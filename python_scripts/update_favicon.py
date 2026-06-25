import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the Cloudinary favicon with our new SVG favicon
    new_content = re.sub(
        r'<link\s+rel="(?:shortcut\s+)?icon"[^>]+>',
        '<link rel="icon" type="image/svg+xml" href="favicon.svg">',
        content,
        flags=re.IGNORECASE
    )
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated favicon in {file}")
    else:
        print(f"No favicon link found to update in {file}")
