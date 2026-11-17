with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function setModel')
if idx != -1:
    print(text[idx:idx+1500])
else:
    print("setModel not found")
