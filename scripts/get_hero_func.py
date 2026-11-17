with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function initHero3dInteractiveTilt()')
end = text.find('function ', pos + 30)
print(text[pos:end])
