with open('styles.css', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('.hero-3d-stage')
if idx != -1:
    print(text[idx:idx+1000])
else:
    print(".hero-3d-stage not found")
