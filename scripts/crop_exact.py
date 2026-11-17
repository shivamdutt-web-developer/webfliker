from PIL import Image
import os

folder = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.user_uploaded'

# In media_1794818784489_0702fcfa.jpg:
im = Image.open(os.path.join(folder, 'media_1794818784489_0702fcfa.jpg'))
# Width 1024, Height 575
# The whole 3D server stack from WordPress sphere to bottom circular pedestal:
# WordPress top is around y=210, pedestal bottom is around y=440
# x goes from roughly 130 to 410
crop_leg = im.crop((130, 210, 410, 440))
crop_leg.save('assets/3d/legacy_stack_exact.png')

# In media_1794818805247_c3d33c8d.jpg (Modern tab on the right):
im_split = Image.open(os.path.join(folder, 'media_1794818805247_c3d33c8d.jpg'))
# In the right half (x: 512-1024), the 4-layer modern tech stack + bag:
# Shopify bag top is around y=200, bottom glow ring is around y=440
# x is roughly 540 to 710
crop_mod = im_split.crop((540, 200, 710, 440))
crop_mod.save('assets/3d/modern_stack_4l_exact.png')

print("Saved exact crops!")
