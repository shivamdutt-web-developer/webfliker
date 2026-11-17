from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

body = soup.find('body')
for s in body.find_all(['section', 'div'], recursive=False):
    classes = s.get('class', [])
    elem_id = s.get('id', '')
    style = s.get('style', '')
    bg_match = re.search(r'background(?:-color)?:\s*([^;]+)', style)
    bg = bg_match.group(1).strip() if bg_match else '(from CSS class)'
    if 'section' in ' '.join(classes) or 'section' in s.name:
        print(f"Section: {elem_id or ' '.join(classes):<32} | BG: {bg}")
