import os
import json
import urllib.request
import re
import glob

print("Loading mapping...")
with open("mapping.json", "r") as f:
    mapping = json.load(f)

# 1. Fix Cover Images
print("Fixing cover images by size matching...")
covers = [k for k in mapping.keys() if k.startswith("cover_")]
remote_covers = {}
for c in covers:
    url = mapping[c]["secure_url"]
    opt_url = url.replace("/upload/", "/upload/f_auto,q_auto/")
    # fetch size
    req = urllib.request.Request(url, method='HEAD')
    try:
        res = urllib.request.urlopen(req)
        size = int(res.headers['Content-Length'])
        remote_covers[size] = opt_url
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

local_covers = {}
for p in glob.glob("extra_2/*/cover.png"):
    size = os.path.getsize(p)
    local_covers[p] = size

cover_replacements = {}
for p, size in local_covers.items():
    if size in remote_covers:
        # e.g., p = "extra_2/UEL Term-1 Work/cover.png"
        folder = os.path.basename(os.path.dirname(p))
        cover_replacements[folder] = remote_covers[size]
        print(f"Matched {folder} to {remote_covers[size]} (size {size})")
    else:
        print(f"Could not match {p} (size {size})")

# Map folder to class
folder_to_class = {
    "UEL Term-1 Work": (".p1", "portfolio1.html"),
    "UEL Term-2 Work": (".p2", "portfolio2.html"),
    "Interior Technical Drawings": (".p3", "portfolio3.html"),
    "Architectural Drawings": (".p4", "portfolio4.html"),
    "Design": (".p5", "portfolio5.html")
}

# Update style.css
with open("style.css", "r") as f:
    style_content = f.read()

for folder, url in cover_replacements.items():
    cls_name, html_file = folder_to_class[folder]
    # Replace background URL for cls_name in style.css
    pattern = re.compile(rf"({cls_name}\s*{{[^}}]*background:\s*url\()\"[^\"]+\"(\))")
    style_content = pattern.sub(rf"\1\"{url}\"\2", style_content)

with open("style.css", "w") as f:
    f.write(style_content)
print("Updated style.css")

# Update HTML files for covers
for folder, url in cover_replacements.items():
    cls_name, html_file = folder_to_class[folder]
    with open(html_file, "r") as f:
        html = f.read()
    html = re.sub(r'(<img src=")[^"]+(" alt="Cover Image")', rf'\g<1>{url}\g<2>', html)
    with open(html_file, "w") as f:
        f.write(html)
    print(f"Updated cover in {html_file}")

# 2. Fix Portfolio1 "Group C" Images
print("\nFixing Term 1 Group C images...")
def normalize(name):
    return re.sub(r'[^a-zA-Z0-9]', '', name).lower()

with open("portfolio1.html", "r") as f:
    p1_html = f.read()

def replace_p1_img(match):
    src = match.group(1)
    if "Group C" in src and not src.startswith("http"):
        base_name = os.path.splitext(os.path.basename(src))[0]
        norm = normalize(base_name)
        for k in mapping.keys():
            if normalize(k) == norm:
                url = mapping[k]["secure_url"].replace("/upload/", "/upload/f_auto,q_auto/")
                # Add lazy loading if missing
                full_tag = match.group(0).replace(f'src="{src}"', f'src="{url}"')
                if 'loading=' not in full_tag:
                    full_tag = full_tag.replace('>', ' loading="lazy">')
                print(f"Mapped {base_name} to {url}")
                return full_tag
        print(f"WARNING: Could not map {base_name}")
    return match.group(0)

p1_html = re.sub(r'<img\s+[^>]*src="([^"]+)"[^>]*>', replace_p1_img, p1_html)
with open("portfolio1.html", "w") as f:
    f.write(p1_html)
print("Updated portfolio1.html images")
