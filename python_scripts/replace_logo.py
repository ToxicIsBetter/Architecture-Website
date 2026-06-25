import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    def replace_logo_container(match):
        container_tag = match.group(1)
        return container_tag + '\n            <span class="site-logo-text" style="font-size: 1.8rem; font-weight: 700; letter-spacing: 1px; color: var(--text-color);">SM</span>\n        </div>'

    new_content = re.sub(r'(<div class="(?:nav-logo|footer-logo)">)\s*<img[^>]+>\s*<img[^>]+>\s*</div>', replace_logo_container, content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"No changes in {file}")
