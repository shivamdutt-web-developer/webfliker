import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<section[^>]*id="founder-spotlight".*?</section>', html, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("founder-spotlight not found by id")
    # let's search for Navneet Kaushal
    m2 = re.search(r'<section[^>]*>.*?Navneet Kaushal.*?</section>', html, re.DOTALL)
    if m2:
        print(m2.group(0)[:1500])
    else:
        print("Navneet Kaushal not found in any section")
