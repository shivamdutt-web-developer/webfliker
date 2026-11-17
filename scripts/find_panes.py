with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

s_leg = html.find('class="trans-3d-visual-pane legacy-visual-pane"')
s_mod = html.find('class="trans-3d-visual-pane modern-visual-pane"')

print(f"s_leg={s_leg}, s_mod={s_mod}")
if s_leg != -1:
    print("Legacy snippet:", html[s_leg:s_leg+150])
if s_mod != -1:
    print("Modern snippet:", html[s_mod:s_mod+150])
