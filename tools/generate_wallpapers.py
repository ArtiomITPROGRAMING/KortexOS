import os
import math
from PIL import Image, ImageDraw

def create_wallpapers(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    w, h = 1920, 1080

    # 1. CYBER GRID (Hacker / Cyber-Deck)
    img_grid = Image.new("RGB", (w, h), (7, 10, 15))
    draw = ImageDraw.Draw(img_grid, "RGBA")

    # Radial vignette / glow in center
    cx, cy = w // 2, h // 2
    for r in range(600, 0, -20):
        alpha = int(25 * (1 - r / 600))
        draw.ellipse([cx - r * 1.6, cy - r, cx + r * 1.6, cy + r], fill=(0, 60, 80, alpha))

    # Grid lines (50px spacing)
    for x in range(0, w, 60):
        alpha = 30 if x % 180 == 0 else 12
        draw.line([(x, 0), (x, h)], fill=(0, 240, 255, alpha), width=1)

    for y in range(0, h, 60):
        alpha = 30 if y % 180 == 0 else 12
        draw.line([(0, y), (w, y)], fill=(0, 240, 255, alpha), width=1)

    # Grid intersection crosshairs
    for x in range(0, w, 180):
        for y in range(0, h, 180):
            draw.line([(x - 6, y), (x + 6, y)], fill=(0, 240, 255, 90), width=1)
            draw.line([(x, y - 6), (x, y + 6)], fill=(0, 240, 255, 90), width=1)

    grid_path = os.path.join(out_dir, "cyber_grid.png")
    img_grid.save(grid_path, "PNG")
    print(f"[+] Created: {grid_path}")

    # 2. MACBOOK GLASS / CYBER CARBON (MacBook UX Mode)
    img_mac = Image.new("RGB", (w, h), (14, 17, 23))
    draw_mac = ImageDraw.Draw(img_mac, "RGBA")

    # Deep multi-radial mesh gradients for glassmorphism
    for r in range(800, 0, -25):
        alpha = int(45 * (1 - r / 800))
        # Top-left deep cyan/blue
        draw_mac.ellipse([-100 - r, -100 - r, -100 + r * 1.8, -100 + r * 1.2], fill=(0, 100, 160, alpha))
        # Bottom-right violet/purple glow
        draw_mac.ellipse([w - r * 1.5, h - r * 1.2, w + r, h + r], fill=(80, 20, 120, alpha))

    mac_path = os.path.join(out_dir, "cyber_glass.png")
    img_mac.save(mac_path, "PNG")
    print(f"[+] Created: {mac_path}")

    # 3. PITCH BLACK (Minimalist OLED)
    img_black = Image.new("RGB", (w, h), (0, 0, 0))
    black_path = os.path.join(out_dir, "pitch_black.png")
    img_black.save(black_path, "PNG")
    print(f"[+] Created: {black_path}")

if __name__ == "__main__":
    out = os.path.abspath("profile/airootfs/usr/share/kortex/wallpapers")
    create_wallpapers(out)
