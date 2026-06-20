import glob
import os

replacements = {
    'Sanskruti.jpeg': 'https://res.cloudinary.com/dfduodbpa/image/upload/f_auto,q_auto,g_face,c_fill/v1781918355/Sanskruti_x1wmhh.jpg',
    'light_logo.png': 'https://res.cloudinary.com/dfduodbpa/image/upload/f_auto,q_auto/v1781918355/light_logo_r6elzy.png',
    'Logo.ico': 'https://res.cloudinary.com/dfduodbpa/image/upload/f_auto,q_auto/v1781918355/Logo_duxuxk.ico',
    'Logo.png': 'https://res.cloudinary.com/dfduodbpa/image/upload/f_auto,q_auto/v1781918355/Logo_zcargy.png'
}

html_files = glob.glob("*.html")
for file in html_files:
    print(f"Processing {file}...")
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_html = html
    for old, new in replacements.items():
        # Replace src="old" and href="old" (for favicon)
        new_html = new_html.replace(f'src="{old}"', f'src="{new}"')
        new_html = new_html.replace(f'href="{old}"', f'href="{new}"')
        
    if new_html != html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"  -> Updated {file}")
    else:
        print(f"  -> No changes for {file}")

print("Done replacing.")
