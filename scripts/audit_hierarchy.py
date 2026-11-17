from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("All top-level sections / containers:")
for elem in soup.find('main', class_='site-main').find_all(['section', 'div'], recursive=False):
    classes = elem.get('class', [])
    elem_id = elem.get('id', '')
    h2 = elem.find(['h1', 'h2', 'h3'])
    h_text = h2.get_text(strip=True) if h2 else ''
    print(f"- Tag: {elem.name} | ID: {elem_id} | Class: {' '.join(classes)} | Heading: {h_text[:60]}")
