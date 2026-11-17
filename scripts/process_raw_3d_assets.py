import numpy as np
from PIL import Image, ImageFilter
import os

folder = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.user_uploaded'
dual_im = Image.open(os.path.join(folder, 'media_1794815255829_f19eb178.jpg')).convert('RGBA')
split_im = Image.open(os.path.join(folder, 'media_1794818805247_c3d33c8d.jpg')).convert('RGBA')

# 1. Legacy 3D Server Stack
# In dual_im, let's locate the exact bounding box of the server stack + wordpress + warning triangle
# In dual_im (1024, 575):
# Legacy card starts around x=60, y=170.
# The server stack is at x: 80 to 240, y: 260 to 445.
# Let's crop x: 75 to 245, y: 255 to 445 (width 170, height 190)
crop_legacy = dual_im.crop((75, 255, 245, 445))

# In this crop, the card background is nearly white (RGB > 245, 240, 240)
# We can make the background transparent with a smooth alpha mask!
arr = np.array(crop_legacy, dtype=np.float32)
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]

# The server stack itself has shadows and colored elements (WordPress blue, Warning red, LEDs red, metallic sides)
# The background is very light peach/white: r > 248, g > 240, b > 238
# Let's compute distance to background color (253, 245, 243)
bg_color = np.array([253, 247, 245], dtype=np.float32)
dist = np.sqrt((r - bg_color[0])**2 + (g - bg_color[1])**2 + (b - bg_color[2])**2)

# If dist < 8, alpha = 0. If dist > 25, alpha = 255. In between, smooth gradient.
alpha = np.clip((dist - 8.0) / 16.0, 0.0, 1.0) * 255.0

# Keep the warning sign glow and server shadow
# Also make sure inside elements don't get keyed out (only edges)
# No scipy needed
crop_legacy.save('assets/3d/legacy_stack_raw.png')

# 2. Modern 4-layer 3D Tech Stack from split_im:
# In split_im (1024, 575), the right side is x: 512 to 1024.
# The 4-layer stack (Shopify Plus, Next.js, WebGL 3D, LLM Graph + bag) is at:
# x: 540 to 710, y: 205 to 445 (width 170, height 240)
crop_modern_4l = split_im.crop((540, 205, 715, 445))
crop_modern_4l.save('assets/3d/modern_stack_4l_raw.png')

# 3. Center Chevron button from dual_im:
# x: 465 to 525, y: 285 to 345 (60x60)
crop_chevron = dual_im.crop((465, 285, 525, 345))
crop_chevron.save('assets/3d/center_chevron_raw.png')

# 4. Floating Torus Rings:
# Left Torus: x: 10 to 125, y: 70 to 175
crop_torus_l = dual_im.crop((12, 70, 125, 175))
crop_torus_l.save('assets/3d/torus_left_raw.png')

# Right Torus: x: 875 to 985, y: 20 to 130
crop_torus_r = dual_im.crop((875, 20, 985, 130))
crop_torus_r.save('assets/3d/torus_right_raw.png')

print("Saved raw assets successfully!")
