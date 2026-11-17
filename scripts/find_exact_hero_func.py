with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function initHero3dInteractiveTilt()')
# Let's count open/close braces
open_b = 0
found_first = False
end_idx = pos
for i in range(pos, len(text)):
    if text[i] == '{':
        open_b += 1
        found_first = True
    elif text[i] == '}':
        open_b -= 1
        if found_first and open_b == 0:
            end_idx = i + 1
            break

print(f"Start: {pos}, End: {end_idx}, Length: {end_idx - pos}")
print("Function code:")
print(text[pos:end_idx])
