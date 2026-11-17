with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

t_left_start = html.find('<div class="trans-3d-bg-element torus-top-left"')
t_right_end_marker = '<div class="container trans-content-container">'
t_right_end = html.find(t_right_end_marker, t_left_start)

torus_replacement = '''<div class="trans-3d-bg-element torus-top-left" aria-hidden="true">
      <img src="assets/3d/torus_left_photoreal.png" alt="" class="bg-torus-img torus-img-left">
    </div>

    <div class="trans-3d-bg-element torus-top-right" aria-hidden="true">
      <img src="assets/3d/torus_right_photoreal.png" alt="" class="bg-torus-img torus-img-right">
    </div>

    '''

if t_left_start != -1 and t_right_end != -1:
    html = html[:t_left_start] + torus_replacement + html[t_right_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced background toruses with photoreal 3D elements!")
else:
    print("Markers not found!")
