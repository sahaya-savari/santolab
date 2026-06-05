from bs4 import BeautifulSoup
import re

html_path = 'index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Fix 1: Duplicate SVG IDs
print("Fixing duplicate IDs...")
id_map = {}
for tag in soup.find_all(id=True):
    orig_id = tag['id']
    if orig_id not in id_map:
        id_map[orig_id] = 1
    else:
        id_map[orig_id] += 1
        new_id = f"{orig_id}_{id_map[orig_id]}"
        tag['id'] = new_id

# Fix 2: Hidden field accessibility
print("Fixing hidden fields...")
for hidden_input in soup.find_all('input', type='hidden'):
    if not hidden_input.has_attr('aria-hidden'):
        hidden_input['aria-hidden'] = 'true'

# Fix 5: Invalid Preload URLs
print("Fixing preload URLs...")
for link in soup.find_all('link', rel='preload'):
    if link.get('href') == 'javascript:void(0)':
        link.decompose()

# Save
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("HTML fixes applied.")
