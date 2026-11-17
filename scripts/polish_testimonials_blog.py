with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Testimonial cards
html = html.replace('<div class="testimonial-card">', '<div class="testimonial-card tilt-card">')

# Blog cards
old_blog_card = '<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; overflow: hidden; box-shadow: 0 4px 20px rgba(15,23,42,0.04);">'
new_blog_card = '<div class="tilt-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 24px; overflow: hidden; box-shadow: 0 8px 24px rgba(15,23,42,0.04); transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease, border-color 0.35s ease;">'
html = html.replace(old_blog_card, new_blog_card)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Testimonials and Blog cards updated with tilt-card!")
