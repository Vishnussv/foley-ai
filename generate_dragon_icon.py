from PIL import Image, ImageDraw

def create_dragon_icon(path):
    # Create a 512x512 image with a transparent background
    img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    cyan = (0, 243, 255, 255)
    dark_cyan = (0, 100, 120, 255)
    glow_cyan = (0, 243, 255, 100)
    
    # Outer ring
    draw.ellipse([20, 20, 492, 492], outline=glow_cyan, width=2)
    draw.ellipse([40, 40, 472, 472], outline=glow_cyan, width=1)
    
    # Stylized Dragon Head (Polygons)
    # Head Base
    head_poly = [
        (256, 100), # Top
        (180, 200), # Left Upper
        (150, 280), # Left Mid
        (180, 320), # Left Lower
        (256, 420), # Bottom (Jaw)
        (332, 320), # Right Lower
        (362, 280), # Right Mid
        (332, 200)  # Right Upper
    ]
    draw.polygon(head_poly, fill=cyan, outline=(255, 255, 255, 150))
    
    # Horns
    left_horn = [(230, 110), (190, 50), (210, 150)]
    right_horn = [(282, 110), (322, 50), (302, 150)]
    draw.polygon(left_horn, fill=dark_cyan)
    draw.polygon(right_horn, fill=dark_cyan)
    
    # Eyes
    draw.polygon([(210, 220), (240, 250), (225, 260)], fill=(255, 255, 255, 255))
    draw.polygon([(302, 220), (272, 250), (287, 260)], fill=(255, 255, 255, 255))
    
    # Tech accents
    draw.line([256, 100, 256, 420], fill=dark_cyan, width=2)
    draw.line([180, 200, 332, 200], fill=dark_cyan, width=1)
    
    img.save(path)
    print(f"Branded dragon icon saved to {path}")

if __name__ == "__main__":
    create_dragon_icon('c:/Users/User/.gemini/antigravity/scratch/jarvis_assistant/backend/static/images/foleydraco_head.png')
