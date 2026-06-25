import os
import requests
from PIL import Image, ImageDraw, ImageFont
import glob

# 1. Download Montserrat Bold font
font_url = "https://github.com/google/fonts/raw/main/ofl/montserrat/Montserrat-Bold.ttf"
font_path = "Montserrat-Bold.ttf"

if not os.path.exists(font_path):
    print("Downloading Montserrat-Bold font...")
    response = requests.get(font_url)
    with open(font_path, "wb") as f:
        f.write(response.content)

# 2. Generate Favicon
size = 256
img = Image.new('RGB', (size, size), color=(255, 255, 255))
d = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype(font_path, 150)
except Exception as e:
    print(f"Error loading font: {e}")
    font = ImageFont.load_default()

text = "SM"
# Calculate bounding box for centering
bbox = d.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]

# Text placement
x = (size - text_w) / 2 - bbox[0]
y = (size - text_h) / 2 - bbox[1]

d.text((x, y), text, fill=(0, 0, 0), font=font)

# Save
img.save("favicon.png")
img.save("favicon.ico", format="ICO", sizes=[(32, 32), (64, 64), (128, 128), (256, 256)])
print("Created favicon.png and favicon.ico")

# 3. Update HTML files to use the local favicon
html_files = glob.glob("*.html")

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We want to replace the current favicon link
    import re
    # The current pattern might look like:
    # <link rel="shortcut icon"
    #     href="https://res.cloudinary.com/.../Logo_duxuxk.ico">
    # We will replace anything matching <link rel="shortcut icon"[^>]+>
    
    def replace_favicon(match):
        return '<link rel="icon" type="image/png" href="favicon.png">'
    
    new_content = re.sub(r'<link\s+rel="(?:shortcut\s+)?icon"[^>]+>', replace_favicon, content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated favicon in {file}")
    else:
        print(f"No favicon link found to update in {file}")

print("Done!")
