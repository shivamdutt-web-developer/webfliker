from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

buttons = soup.find_all(['a', 'button'])
btn_list = []
for b in buttons:
    classes = b.get('class', [])
    style = b.get('style', '')
    text = b.get_text(strip=True)
    if any('btn' in c for c in classes) or 'btn' in style or any('cta' in c for c in classes) or len(text) > 0 and len(text) < 40:
        parent_sec = b.find_parent('section')
        sec_id = parent_sec.get('id', 'no-id') if parent_sec else 'no-sec'
        btn_list.append({
            'sec': sec_id,
            'tag': b.name,
            'class': ' '.join(classes),
            'style': style,
            'text': text[:35]
        })

print(f"Total buttons/CTAs found: {len(btn_list)}")
for b in btn_list[:25]:
    print(f"[{b['sec']}] <{b['tag']} class='{b['class']}' style='{b['style']}'> -> {b['text']}")
