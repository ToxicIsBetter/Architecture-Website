import re
import json
import os

print("Swapping cover images for portfolio 2 and 4...")

# From our previous analysis:
# portfolio2 was using: v1781912390/cover_vetv06.png
# portfolio4 was using: v1781913238/cover_vp5ig8.png
url_2 = "https://res.cloudinary.com/dfduodbpa/image/upload/f_auto,q_auto/v1781912390/cover_vetv06.png"
url_4 = "https://res.cloudinary.com/dfduodbpa/image/upload/f_auto,q_auto/v1781913238/cover_vp5ig8.png"

def swap_html(filename, expected_url, new_url):
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
    if expected_url in content:
        content = content.replace(expected_url, new_url)
        with open(filename, "w", encoding='utf-8') as f:
            f.write(content)
        print(f"Swapped in {filename}")
    else:
        print(f"Warning: expected URL not found in {filename}")

swap_html("portfolio2.html", url_2, url_4)
swap_html("portfolio4.html", url_4, url_2)

def swap_css(filename):
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
    
    # We find .p2 block and replace url_2 with url_4, and .p4 block to replace url_4 with url_2
    # Simple replace is safe because the URLs are completely unique
    content = content.replace(url_2, "TEMP_SWAP_URL")
    content = content.replace(url_4, url_2)
    content = content.replace("TEMP_SWAP_URL", url_4)
    
    with open(filename, "w", encoding='utf-8') as f:
        f.write(content)
    print(f"Swapped in {filename}")

swap_css("style.css")

print("\nFixing portfolio1.html Term 1 images...")
with open("mapping.json", "r") as f:
    mapping = json.load(f)

def normalize(name):
    # keep only alphanumeric
    return re.sub(r'[^a-zA-Z0-9]', '', name).lower()

with open("portfolio1.html", "r", encoding='utf-8') as f:
    p1_html = f.read()

def replace_p1_img(match):
    full_tag = match.group(0)
    src = match.group(1)
    
    if src.startswith("http") or "Logo" in src or "light_logo" in src or "Sanskruti" in src:
        return full_tag
        
    base_name = os.path.splitext(os.path.basename(src))[0]
    norm = normalize(base_name)
    
    for k in mapping.keys():
        clean_k = re.sub(r'_[a-z0-9]{6}$', '', k)
        if normalize(clean_k) == norm:
            print(f"Match found: {clean_k} == {norm}")
            url = mapping[k][0] if isinstance(mapping[k], list) else mapping[k].get("secure_url")
            opt_url = url.replace("/upload/", "/upload/f_auto,q_auto/")
            
            # replace src
            new_tag = full_tag.replace(f'src="{src}"', f'src="{opt_url}"')
            if 'loading=' not in new_tag:
                new_tag = new_tag.replace('>', ' loading="lazy">')
            
            print(f"Mapped: {base_name} -> {opt_url}")
            return new_tag
            
    print(f"WARNING: Could not map {base_name} (norm: {norm})")
    return full_tag

# Only replace non-Cloudinary images
img_pattern = re.compile(r'<img\s+[^>]*src="([^"]+)"[^>]*>')
p1_html_new = img_pattern.sub(replace_p1_img, p1_html)

if p1_html_new != p1_html:
    with open("portfolio1.html", "w", encoding='utf-8') as f:
        f.write(p1_html_new)
    print("Updated portfolio1.html images!")
else:
    print("No changes made to portfolio1.html images.")
