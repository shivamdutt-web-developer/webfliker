with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('<!-- Hero Right: POLISHED 3-ELEMENT 3D HERO SHOWCASE -->')
print(text[start_idx+3300:start_idx+4500])
