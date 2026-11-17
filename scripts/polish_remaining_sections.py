with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Pricing Cards
html = html.replace('<div class="plan-card">', '<div class="plan-card tilt-card">')
html = html.replace('<div class="plan-card popular">', '<div class="plan-card popular tilt-card">')

# 2. Milestones
html = html.replace(
    '<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 28px 24px; box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04); position: relative;">',
    '<div class="timeline-milestone-card tilt-card">'
)
html = html.replace(
    '<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 28px 24px; box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);">',
    '<div class="timeline-milestone-card tilt-card">'
)
html = html.replace(
    '<div style="background: linear-gradient(135deg, #0f172a, #1e293b); color: #ffffff; border: 1px solid rgba(255, 94, 30, 0.4); border-radius: 20px; padding: 28px 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">',
    '<div class="timeline-milestone-card ai-highlight tilt-card">'
)

# 3. Scanner box
html = html.replace('<div class="scanner-box-card">', '<div class="scanner-box-card tilt-card">')

# 4. Global Hubs
html = html.replace(
    '<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 20px; padding: 32px 28px; box-shadow: 0 4px 20px rgba(15,23,42,0.04); transition: transform 0.3s ease;">',
    '<div class="hub-card tilt-card">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Remaining sections updated with tilt-card and high-end classes!")
