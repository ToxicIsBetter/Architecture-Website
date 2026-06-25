import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove ALL favicon.svg links
    content = re.sub(r'\s*<link rel="icon" type="image/svg\+xml" href="favicon\.svg">', '', content)
    
    # Insert EXACTLY ONE favicon.svg link right before </head>
    content = content.replace("</head>", '    <link rel="icon" type="image/svg+xml" href="favicon.svg">\n</head>')
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cleaned up {file}")
