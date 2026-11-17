import os
for f in os.listdir('.'):
    if f.endswith('.py') or f.endswith('.js') or f.endswith('.md'):
        print(f)
