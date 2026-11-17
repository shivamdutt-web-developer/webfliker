from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

for b in soup.find_all(['a', 'button']):
    classes = b.get('class', [])
    style = b.get('style', '')
    text = b.get_text(strip=True)
    parent_sec = b.find_parent('section')
    if parent_sec:
        sec_id = parent_sec.get('id', parent_sec.get('class', ['no-class'])[0])
        if any(c in ' '.join(classes) for c in ['btn', 'link', 'tab', 'action']) or b.name == 'button':
            print(f"[{sec_id}] <{b.name} class='{' '.join(classes)}' style='{style}'> -> '{text}'")
