with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function initThreeJsLab')
end_idx = text.find('function init3dCardTilt')
print(text[idx:end_idx])
