from bs4 import BeautifulSoup
import re

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = []
for el in soup.find_all(True):
    classes = el.get('class', [])
    for c in classes:
        if 'card' in c or 'box' in c or 'tier' in c or 'item' in c:
            if c not in cards and not c.startswith('lucide'):
                cards.append(c)

print('Card/box classes found:', cards[:30])
