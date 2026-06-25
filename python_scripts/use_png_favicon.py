import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the SVG favicon with PNG favicon
    content = re.sub(r'<link rel="icon" type="image/svg\+xml" href="favicon\.svg">', '<link rel="icon" type="image/png" href="favicon.png">', content)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated favicon to PNG in {file}")
