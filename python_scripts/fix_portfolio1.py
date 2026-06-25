import json

with open("mapping.json", "r") as f:
    mapping = json.load(f)

with open("portfolio1.html", "r", encoding='utf-8') as f:
    html = f.read()

# For each 'Group C - Adrija, Prakruti, Sanskruti, Zahra XX of 32.png',
# we find its Cloudinary URL in mapping.json and replace it in the HTML.
# The local name format is: UEL Term-1 Work/Group C - Adrija, Prakruti, Sanskruti, Zahra {num} of 32.png
# The Cloudinary name format is: Group_C_-_Adrija_Prakruti_Sanskruti_Zahra_{num}_of_32_{random}.png

changes_made = False

for num in [8, 9, 10, 12, 17, 18, 19, 22, 25, 27, 29, 31]:
    local_path = f'UEL Term-1 Work/Group C - Adrija, Prakruti, Sanskruti, Zahra {num} of 32.png'
    
    # Find matching Cloudinary URL
    prefix = f"Group_C_-_Adrija_Prakruti_Sanskruti_Zahra_{num}_of_32_"
    matched_url = None
    
    for k, v in mapping.items():
        if k.startswith(prefix):
            matched_url = v[0] if isinstance(v, list) else v.get("secure_url")
            break
            
    if matched_url:
        opt_url = matched_url.replace("/upload/", "/upload/f_auto,q_auto/")
        if local_path in html:
            html = html.replace(local_path, opt_url)
            changes_made = True
            print(f"Replaced {num} of 32")
        else:
            print(f"Warning: {local_path} not found in HTML!")
    else:
        print(f"Warning: No Cloudinary match found for {local_path}!")

if changes_made:
    with open("portfolio1.html", "w", encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated portfolio1.html!")
else:
    print("No changes made.")
