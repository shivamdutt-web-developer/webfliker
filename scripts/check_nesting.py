from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')
hero = soup.find('section', id='hero')
print("Hero found:", hero is not None)
if hero:
    stage = hero.find(id='hero3dStage')
    print("Stage inside hero:", stage is not None)
    if stage:
        scene = stage.find(id='hero3dScene')
        print("Scene inside stage:", scene is not None)
