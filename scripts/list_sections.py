import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*id="([^"]+)"', html)
print('All section IDs in order:')
for i, s in enumerate(sections):
    print(f"{i}: #{s}")
