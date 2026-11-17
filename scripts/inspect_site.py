import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', html)
print("Sections with ID:", sections)

all_sections = re.findall(r'<section[^>]*class=["\']([^"\']+)["\']', html)
print("\nSection classes:")
for sc in all_sections:
    print(" -", sc)
