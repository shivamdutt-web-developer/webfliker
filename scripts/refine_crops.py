from PIL import Image, ImageFilter
import numpy as np
import os

folder = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.user_uploaded'

# 1. Refined Modern 4-Layer Tech Stack:
im_mod = Image.open(os.path.join(folder, 'media_1794818805247_c3d33c8d.jpg')).convert('RGBA')
# Start y at 214 (just below the green pill badge) to 445
# x from 556 to 715
crop_mod = im_mod.crop((556, 214, 715, 445))

wm, hm = crop_mod.size
mod_mask_arr = np.ones((hm, wm), dtype=np.float32)
mod_mask_arr[:, :8] *= np.linspace(0, 1, 8)
mod_mask_arr[:, -8:] *= np.linspace(1, 0, 8)
mod_mask_arr[:8, :] *= np.linspace(0, 1, 8)[:, None]
mod_mask_arr[-8:, :] *= np.linspace(1, 0, 8)[:, None]

mod_feathered_mask = Image.fromarray((mod_mask_arr * 255).astype(np.uint8), mode='L').filter(ImageFilter.GaussianBlur(2))
crop_mod.putalpha(mod_feathered_mask)
crop_mod.save('assets/3d/modern_tech_3d_photoreal.png')

# 2. Refined Legacy Stack:
im_leg = Image.open(os.path.join(folder, 'media_1794818784489_0702fcfa.jpg')).convert('RGBA')
crop_leg = im_leg.crop((128, 218, 402, 445))
wl, hl = crop_leg.size
leg_mask_arr = np.ones((hl, wl), dtype=np.float32)
leg_mask_arr[:, :10] *= np.linspace(0, 1, 10)
leg_mask_arr[:, -10:] *= np.linspace(1, 0, 10)
leg_mask_arr[:10, :] *= np.linspace(0, 1, 10)[:, None]
leg_mask_arr[-10:, :] *= np.linspace(1, 0, 10)[:, None]

leg_feathered_mask = Image.fromarray((leg_mask_arr * 255).astype(np.uint8), mode='L').filter(ImageFilter.GaussianBlur(2))
crop_leg.putalpha(leg_feathered_mask)
crop_leg.save('assets/3d/legacy_server_3d_photoreal.png')

print("Refined crops saved!")
