from PIL import Image
import os

folder = r'C:\Users\shiva\.gemini\antigravity\brain\2e7d2b96-cdc7-413f-bf71-e57580e857c8\.user_uploaded'
dual_img_path = os.path.join(folder, 'media_1794815255829_f19eb178.jpg')
split_img_path = os.path.join(folder, 'media_1794818805247_c3d33c8d.jpg')

dual_im = Image.open(dual_img_path)
split_im = Image.open(split_img_path)

# Let's crop candidate regions from dual_im
# Left 3D server stack:
# In 1024x575:
# Legacy card is roughly x: 60 to 480, y: 170 to 470
# 3D server stack is inside it on the left: roughly x: 80 to 240, y: 250 to 440
crop_legacy = dual_im.crop((80, 260, 240, 440))
os.makedirs('assets/3d', exist_ok=True)
crop_legacy.save('assets/3d/test_crop_legacy.png')

# Modern 3D tech stack in dual_im:
# Modern card is roughly x: 520 to 960, y: 170 to 470
# 3D stack is roughly x: 550 to 710, y: 250 to 440
crop_modern = dual_im.crop((550, 260, 710, 440))
crop_modern.save('assets/3d/test_crop_modern.png')

# In split_im (which has the 4-layer modern tech stack):
# Right half is x: 512 to 1024
# Inside the right panel, 3D stack is roughly x: 540 to 710, y: 220 to 440
crop_modern_4layer = split_im.crop((540, 210, 710, 440))
crop_modern_4layer.save('assets/3d/test_crop_modern_4layer.png')

# Floating torus left:
crop_torus_l = dual_im.crop((10, 80, 120, 180))
crop_torus_l.save('assets/3d/test_crop_torus_l.png')

# Floating torus right:
crop_torus_r = dual_im.crop((870, 20, 980, 130))
crop_torus_r.save('assets/3d/test_crop_torus_r.png')

# Center glowing chevron:
crop_chevron = dual_im.crop((460, 280, 530, 360))
crop_chevron.save('assets/3d/test_crop_chevron.png')

print("Saved test crops successfully!")
