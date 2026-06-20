import cloudinary
import cloudinary.api
import json

cloudinary.config(
  cloud_name = 'dfduodbpa',
  api_key = '427619153478657',
  api_secret = 'xLobalQq9h8TlG0GZdtqD8rAFEY',
  secure = True
)

mapping = {}
res = cloudinary.api.resources(max_results=500)
for r in res.get('resources', []):
    mapping[r.get('public_id')] = {
        'original_filename': r.get('original_filename'),
        'secure_url': r['secure_url'],
        'folder': r.get('folder', '')
    }

with open('mapping.json', 'w') as f:
    json.dump(mapping, f, indent=2)
print("Done writing mapping.json")
