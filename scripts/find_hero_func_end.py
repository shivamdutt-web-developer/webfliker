with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function initHero3dInteractiveTilt()')
# Find the matching closing bracket or next section header
next_func = text.find('/* ========================================================================= */\n/* 3D TILT PHYSICS', pos)
if next_func == -1:
    next_func = text.find('function init3dCardPhysics()', pos)
print(f"Length of function block: {next_func - pos}")
print(text[pos:pos+1200])
print("... END ...")
print(text[next_func-200:next_func])
