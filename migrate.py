import cloudinary
import cloudinary.api
import glob
import os
import re

cloudinary.config(
  cloud_name = 'dfduodbpa',
  api_key = '427619153478657',
  api_secret = 'xLobalQq9h8TlG0GZdtqD8rAFEY',
  secure = True
)

print("Fetching resources from Cloudinary...")
mapping = {}
next_cursor = None
while True:
    res = cloudinary.api.resources(max_results=500, next_cursor=next_cursor)
    for r in res.get('resources', []):
        public_id = r.get('public_id', '')
        # Cloudinary appends _ and 6 random alphanumeric chars
        # e.g., cover_vp5ig8 -> cover
        # Group_C_-_Adrija_31_of_32_nuq2qq -> Group_C_-_Adrija_31_of_32
        match = re.sub(r'_[a-z0-9]{6}$', '', public_id)
        
        secure_url = r['secure_url']
        lower_match = match.lower()
        if lower_match not in mapping:
            mapping[lower_match] = []
        mapping[lower_match].append(secure_url)

    next_cursor = res.get('next_cursor')
    if not next_cursor:
        break

print(f"Fetched {sum(len(v) for v in mapping.values())} URLs across {len(mapping)} unique base names.")

def optimize_url(url, is_headshot=False):
    parts = url.split('/upload/')
    if len(parts) != 2:
        return url
    
    if is_headshot:
        return f"{parts[0]}/upload/f_auto,q_auto,g_face,c_fill/{parts[1]}"
    else:
        return f"{parts[0]}/upload/f_auto,q_auto/{parts[1]}"

html_files = glob.glob("*.html")
for file in html_files:
    print(f"Processing {file}...")
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    img_pattern = re.compile(r'<img\s+[^>]*src="([^"]+)"[^>]*>')
    
    def replace_img(match_obj):
        full_tag = match_obj.group(0)
        src = match_obj.group(1)
        
        if src.startswith('http') or src.startswith('//') or src.lower().endswith('.svg'):
            return full_tag
            
        base_src = os.path.basename(src)
        name_no_ext = os.path.splitext(base_src)[0]
        is_headshot = ('Sanskruti.jpeg' in src)
        
        # Normalize local name to match Cloudinary (spaces to underscores, lowercased)
        normalized_name = name_no_ext.replace(' ', '_').lower()
        
        new_url = None
        if normalized_name in mapping and len(mapping[normalized_name]) > 0:
            assigned_url = mapping[normalized_name].pop(0)
            new_url = optimize_url(assigned_url, is_headshot)
            
        new_tag = full_tag
        if new_url:
            new_tag = new_tag.replace(f'src="{src}"', f'src="{new_url}"')
        else:
            print(f"  [Warning] No mapping found for: {src} (normalized: {normalized_name})")
        
        # Lazy loading
        if 'site-logo' not in new_tag and 'hero' not in new_tag and 'loading=' not in new_tag:
            new_tag = new_tag[:-1] + ' loading="lazy">'
            
        return new_tag

    new_html = img_pattern.sub(replace_img, html)
    
    if new_html != html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"  -> Updated {file}")
    else:
        print(f"  -> No changes for {file}")

print("Done!")
