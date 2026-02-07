from PIL import Image
import os

png_path = r'c:/Users/User/.gemini/antigravity/scratch/jarvis_assistant/backend/static/images/foleydraco_head.png'
ico_path = r'c:/Users/User/.gemini/antigravity/scratch/jarvis_assistant/foleydraco.ico'

if os.path.exists(png_path):
    img = Image.open(png_path)
    img.save(ico_path, format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    print(f"Icon saved to {ico_path}")
else:
    print("PNG source not found.")
