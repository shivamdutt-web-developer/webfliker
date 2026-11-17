from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

body = soup.find('body')
print("Direct children of body or main sections:")
for elem in body.find_all(['section', 'div'], recursive=False):
    classes = elem.get('class', [])
    elem_id = elem.get('id', '')
    h = elem.find(['h1', 'h2', 'h3'])
    h_text = h.get_text(strip=True) if h else ''
    print(f"- Tag: {elem.name} | ID: {elem_id} | Class: {' '.join(classes)} | Heading: {h_text[:60]}")
