from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print('--- Sections in index.html ---')
for s in soup.find_all(['section', 'header', 'footer']):
    s_id = s.get('id', 'no-id')
    s_class = ' '.join(s.get('class', []))
    h = s.find(['h1', 'h2', 'h3'])
    h_text = h.get_text(strip=True)[:45] if h else 'No heading'
    print(f'<{s.name}> id="{s_id}" class="{s_class}" -> {h_text}')
