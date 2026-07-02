import glob
import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Remove the Cormorant Garamond font-family rule completely from h1, h2, h3, h4 blocks
css = re.sub(r"font-family:\s*['\"]Cormorant Garamond['\"],\s*serif;", "", css)
with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Remove Cormorant Garamond from google fonts link
    html = html.replace("Cormorant+Garamond:wght@300;400;500;600&family=", "")
    html = html.replace("family=Cormorant+Garamond:wght@300;400;500;600&", "")
    html = html.replace("Cormorant+Garamond:wght@300;400;500;600&", "")
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(html)

print("Phase 1 Typography update complete.")
