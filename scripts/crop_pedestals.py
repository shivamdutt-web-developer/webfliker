from PIL import Image
import os

folder = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.user_uploaded'

# 1. From media_1794818784489_0702fcfa.jpg (Image 2 - Legacy Monolith tab)
# The image is 1024x575
im_legacy = Image.open(os.path.join(folder, 'media_1794818784489_0702fcfa.jpg'))
# In im_legacy, the 3D server stack on its round pink pedestal is on the left
# Let's crop x: 130 to 410, y: 320 to 540
crop_leg_pedestal = im_legacy.crop((120, 310, 410, 545))
crop_leg_pedestal.save('assets/3d/legacy_stack_full_pedestal.png')

# 2. From media_1794818805247_c3d33c8d.jpg (Modernized 3D Headless on the right)
im_split = Image.open(os.path.join(folder, 'media_1794818805247_c3d33c8d.jpg'))
# In im_split, the right panel has the 4-layer 3D stack (Shopify Plus, Next.js, WebGL 3D, LLM Graph) on glowing base
# In 1024x575:
# Right panel starts around x: 520, ends around x: 980
# 3D stack is roughly x: 535 to 720, y: 380 to 570 or let's find exact coordinates:
# Let's crop a slightly wider window to inspect
crop_mod_pedestal = im_split.crop((530, 360, 725, 570))
crop_mod_pedestal.save('assets/3d/modern_stack_full_pedestal.png')

# Also from media_1794815255829_f19eb178.jpg (Dual View):
# Modern 3D stack on the right:
im_dual = Image.open(os.path.join(folder, 'media_1794815255829_f19eb178.jpg'))
crop_dual_modern = im_dual.crop((560, 275, 710, 455))
crop_dual_modern.save('assets/3d/dual_modern_stack.png')

crop_dual_legacy = im_dual.crop((90, 275, 235, 455))
crop_dual_legacy.save('assets/3d/dual_legacy_stack.png')

print("Saved pedestal crops!")
