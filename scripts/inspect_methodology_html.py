with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="methodology"')
if idx != -1:
    print(text[idx:idx+2500])
else:
    print("methodology not found")
