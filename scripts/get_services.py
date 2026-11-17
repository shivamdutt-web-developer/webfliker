import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<section[^>]*id="services".*?</section>', html, re.DOTALL)
if m:
    print(m.group(0)[:1500])
else:
    print("Not found")
