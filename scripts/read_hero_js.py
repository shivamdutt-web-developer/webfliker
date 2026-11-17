with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find("document.getElementById('hero3dStage')")
start = text.rfind('function', 0, pos)
print(text[start:start+2500])
