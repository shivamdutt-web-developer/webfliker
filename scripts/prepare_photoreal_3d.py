from PIL import Image, ImageFilter
import numpy as np
import os

folder = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.user_uploaded'

# 1. Legacy Stack with Pedestal from media_1794818784489_0702fcfa.jpg
im_leg = Image.open(os.path.join(folder, 'media_1794818784489_0702fcfa.jpg')).convert('RGBA')
# Bounding box around the 3D server stack and circular pedestal:
# x: 130 to 400, y: 215 to 445 (width: 270, height: 230)
crop_leg = im_leg.crop((130, 215, 400, 445))

# Feather edges to blend seamlessly into #ffffff / #fdfbf7
w, h = crop_leg.size
mask = Image.new('L', (w, h), 255)
# Create a radial/rounded gradient mask for seamless edge blending
mask_arr = np.ones((h, w), dtype=np.float32)
# Fade left edge (0 to 15px)
mask_arr[:, :12] *= np.linspace(0, 1, 12)
# Fade right edge (w-15 to w)
mask_arr[:, -12:] *= np.linspace(1, 0, 12)
# Fade top edge (0 to 12px)
mask_arr[:12, :] *= np.linspace(0, 1, 12)[:, None]
# Fade bottom edge (h-12 to h)
mask_arr[-12:, :] *= np.linspace(1, 0, 12)[:, None]

feathered_mask = Image.fromarray((mask_arr * 255).astype(np.uint8), mode='L').filter(ImageFilter.GaussianBlur(3))
crop_leg.putalpha(feathered_mask)
crop_leg.save('assets/3d/legacy_server_3d_photoreal.png')

# 2. Modern 4-Layer Tech Stack from media_1794818805247_c3d33c8d.jpg
im_mod = Image.open(os.path.join(folder, 'media_1794818805247_c3d33c8d.jpg')).convert('RGBA')
# In right panel, x: 556 to 715, y: 200 to 445 (width: 159, height: 245)
crop_mod = im_mod.crop((556, 200, 715, 445))

# Feather edges to blend seamlessly into #090e1a
wm, hm = crop_mod.size
mod_mask_arr = np.ones((hm, wm), dtype=np.float32)
mod_mask_arr[:, :10] *= np.linspace(0, 1, 10)
mod_mask_arr[:, -10:] *= np.linspace(1, 0, 10)
mod_mask_arr[:10, :] *= np.linspace(0, 1, 10)[:, None]
mod_mask_arr[-10:, :] *= np.linspace(1, 0, 10)[:, None]

mod_feathered_mask = Image.fromarray((mod_mask_arr * 255).astype(np.uint8), mode='L').filter(ImageFilter.GaussianBlur(2.5))
crop_mod.putalpha(mod_feathered_mask)
crop_mod.save('assets/3d/modern_tech_3d_photoreal.png')

# 3. Center Glowing Chevron from media_1794815255829_f19eb178.jpg
im_dual = Image.open(os.path.join(folder, 'media_1794815255829_f19eb178.jpg')).convert('RGBA')
crop_chev = im_dual.crop((468, 285, 526, 343))
wc, hc = crop_chev.size
# Circular mask
circle_mask = Image.new('L', (wc, hc), 0)
from PIL import ImageDraw
draw = ImageDraw.Draw(circle_mask)
draw.ellipse((2, 2, wc-2, hc-2), fill=255)
circle_mask = circle_mask.filter(ImageFilter.GaussianBlur(1.5))
crop_chev.putalpha(circle_mask)
crop_chev.save('assets/3d/center_chevron_photoreal.png')

# 4. Floating Torus Rings:
# Left Torus:
crop_tl = im_dual.crop((18, 75, 115, 170))
# Key out the warm off-white background (#fdfbf8)
tl_arr = np.array(crop_tl, dtype=np.float32)
r, g, b = tl_arr[:,:,0], tl_arr[:,:,1], tl_arr[:,:,2]
# Background is warm cream r>250, g>242, b>238
bg_diff = np.sqrt((r-253)**2 + (g-247)**2 + (b-244)**2)
tl_alpha = np.clip((bg_diff - 12.0) / 18.0, 0.0, 1.0) * 255.0
crop_tl.putalpha(Image.fromarray(tl_alpha.astype(np.uint8), mode='L').filter(ImageFilter.GaussianBlur(1)))
crop_tl.save('assets/3d/torus_left_photoreal.png')

# Right Torus:
crop_tr = im_dual.crop((880, 25, 980, 125))
tr_arr = np.array(crop_tr, dtype=np.float32)
r, g, b = tr_arr[:,:,0], tr_arr[:,:,1], tr_arr[:,:,2]
bg_diff_r = np.sqrt((r-253)**2 + (g-247)**2 + (b-244)**2)
tr_alpha = np.clip((bg_diff_r - 12.0) / 18.0, 0.0, 1.0) * 255.0
crop_tr.putalpha(Image.fromarray(tr_alpha.astype(np.uint8), mode='L').filter(ImageFilter.GaussianBlur(1)))
crop_tr.save('assets/3d/torus_right_photoreal.png')

print("All 3D photoreal assets successfully generated and feathered!")
