import os
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

THEME_DIR = r"profile\airootfs\usr\share\plymouth\themes\kortex-tron"
os.makedirs(THEME_DIR, exist_ok=True)

def create_glow(base_img, blur_radius=3):
    glow = base_img.filter(ImageFilter.GaussianBlur(blur_radius))
    out = Image.new("RGBA", base_img.size, (0, 0, 0, 0))
    out.paste(glow, (0, 0))
    out.paste(base_img, (0, 0), base_img)
    return out

def draw_watermark():
    w, h = 600, 160
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer cybernetic frame
    # Cut corners
    cut = 12
    points = [
        (20 + cut, 20), (w - 20 - cut, 20),
        (w - 20, 20 + cut), (w - 20, h - 20 - cut),
        (w - 20 - cut, h - 20), (20 + cut, h - 20),
        (20, h - 20 - cut), (20, 20 + cut),
        (20 + cut, 20)
    ]
    draw.line(points, fill=(255, 255, 255, 230), width=2)
    
    # Corner tech ticks
    draw.line([(10, 20 + cut), (10, 20), (20, 10), (20 + cut, 10)], fill=(255, 255, 255, 255), width=2)
    draw.line([(w - 10, 20 + cut), (w - 10, 20), (w - 20, 10), (w - 20 - cut, 10)], fill=(255, 255, 255, 255), width=2)
    draw.line([(10, h - 20 - cut), (10, h - 20), (20, h - 10), (20 + cut, h - 10)], fill=(255, 255, 255, 255), width=2)
    draw.line([(w - 10, h - 20 - cut), (w - 10, h - 20), (w - 20, h - 10), (w - 20 - cut, h - 10)], fill=(255, 255, 255, 255), width=2)
    
    # Inner brackets around logo
    # Left bracket
    draw.line([(45, 40), (35, 40), (35, 120), (45, 120)], fill=(255, 255, 255, 255), width=3)
    # Right bracket
    draw.line([(w - 45, 40), (w - 35, 40), (w - 35, 120), (w - 45, 120)], fill=(255, 255, 255, 255), width=3)

    # Procedural geometric cyber font for "KORTEX - OS"
    # Height = 48, center Y = 70 (y0 = 46, y1 = 94)
    y0, y1 = 48, 92
    
    def draw_letter(char, x):
        lw = 24
        thick = 4
        if char == 'K':
            draw.line([(x, y0), (x, y1)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x, (y0+y1)//2), (x + lw, y0)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x + 6, (y0+y1)//2), (x + lw, y1)], fill=(255, 255, 255, 255), width=thick)
        elif char == 'O':
            draw.line([(x + 4, y0), (x + lw - 4, y0)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x + 4, y1), (x + lw - 4, y1)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x, y0 + 4), (x, y1 - 4)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x + lw, y0 + 4), (x + lw, y1 - 4)], fill=(255, 255, 255, 255), width=thick)
            draw.point([(x+1, y0+1), (x+lw-1, y0+1), (x+1, y1-1), (x+lw-1, y1-1)], fill=(255, 255, 255, 255))
        elif char == 'R':
            draw.line([(x, y0), (x, y1)], fill=(255, 255, 255, 255), width=thick)
            mid = (y0 + y1) // 2
            draw.line([(x, y0), (x + lw - 4, y0)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x + lw, y0 + 4), (x + lw, mid - 2)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x, mid), (x + lw - 4, mid)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x + 6, mid), (x + lw, y1)], fill=(255, 255, 255, 255), width=thick)
        elif char == 'T':
            draw.line([(x, y0), (x + lw, y0)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x + lw//2, y0), (x + lw//2, y1)], fill=(255, 255, 255, 255), width=thick)
        elif char == 'E':
            draw.line([(x, y0), (x, y1)], fill=(255, 255, 255, 255), width=thick)
            mid = (y0 + y1) // 2
            draw.line([(x, y0), (x + lw, y0)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x, mid), (x + lw - 6, mid)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x, y1), (x + lw, y1)], fill=(255, 255, 255, 255), width=thick)
        elif char == 'X':
            draw.line([(x, y0), (x + lw, y1)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x + lw, y0), (x, y1)], fill=(255, 255, 255, 255), width=thick)
        elif char == '-':
            mid = (y0 + y1) // 2
            draw.line([(x + 4, mid), (x + lw - 4, mid)], fill=(255, 255, 255, 255), width=thick)
        elif char == 'S':
            mid = (y0 + y1) // 2
            draw.line([(x + 4, y0), (x + lw, y0)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x, y0 + 3), (x, mid - 2)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x + 2, mid), (x + lw - 2, mid)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x + lw, mid + 2), (x + lw, y1 - 3)], fill=(255, 255, 255, 255), width=thick)
            draw.line([(x, y1), (x + lw - 4, y1)], fill=(255, 255, 255, 255), width=thick)
        return lw + 14

    letters = "KORTEX-OS"
    # Calculate starting x
    total_w = len(letters) * 38
    cur_x = (w - total_w) // 2
    for char in letters:
        adv = draw_letter(char, cur_x)
        cur_x += adv

    # Subtitle: "INTELLIGENCE SYSTEM"
    try:
        font = ImageFont.truetype("arial.ttf", 11)
        sub_text = "INTELLIGENCE SYSTEM // v1.0.0 HYBRID KERNEL"
        bbox = draw.textbbox((0, 0), sub_text, font=font)
        sub_w = bbox[2] - bbox[0]
        draw.text(((w - sub_w) // 2, 115), sub_text, fill=(200, 200, 200, 220), font=font)
    except Exception:
        pass

    # Glow effect
    final_img = create_glow(img, blur_radius=2)
    final_img.save(os.path.join(THEME_DIR, "watermark.png"))
    final_img.save(os.path.join(THEME_DIR, "logo.png"))
    print("[+] Watermark and logo generated.")

def draw_throbber_frames():
    size = 120
    center = size // 2
    radius = 38
    num_frames = 30
    
    for frame in range(num_frames):
        img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        base_angle = (frame / num_frames) * 360.0
        
        # Center reticle (+)
        draw.line([(center - 6, center), (center - 2, center)], fill=(255, 255, 255, 160), width=1)
        draw.line([(center + 2, center), (center + 6, center)], fill=(255, 255, 255, 160), width=1)
        draw.line([(center, center - 6), (center, center - 2)], fill=(255, 255, 255, 160), width=1)
        draw.line([(center, center + 2), (center, center + 6)], fill=(255, 255, 255, 160), width=1)
        
        # Inner segmented circle (16 small ticks)
        for i in range(16):
            ang = math.radians(i * (360 / 16))
            r_in = radius - 10
            r_out = radius - 7
            x1 = center + r_in * math.cos(ang)
            y1 = center + r_in * math.sin(ang)
            x2 = center + r_out * math.cos(ang)
            y2 = center + r_out * math.sin(ang)
            draw.line([(x1, y1), (x2, y2)], fill=(255, 255, 255, 50), width=1)
            
        # Outer scanner arc: 240 degrees, gradient tail
        segments = 36
        arc_span = 260
        for seg in range(segments):
            frac = seg / segments
            # Angle of this segment
            seg_angle = base_angle + (frac * arc_span)
            alpha = int(255 * (frac ** 1.8))
            width = 2 if frac < 0.8 else 3
            
            ang1 = math.radians(seg_angle)
            ang2 = math.radians(seg_angle + (arc_span / segments) + 0.5)
            
            x1 = center + radius * math.cos(ang1)
            y1 = center + radius * math.sin(ang1)
            x2 = center + radius * math.cos(ang2)
            y2 = center + radius * math.sin(ang2)
            
            draw.line([(x1, y1), (x2, y2)], fill=(255, 255, 255, alpha), width=width)
            
        # Leading bright beacon dot
        head_ang = math.radians(base_angle + arc_span)
        hx = center + radius * math.cos(head_ang)
        hy = center + radius * math.sin(head_ang)
        draw.ellipse([(hx - 3, hy - 3), (hx + 3, hy + 3)], fill=(255, 255, 255, 255))
        
        glow_img = create_glow(img, blur_radius=2)
        frame_name = f"throbber-{frame+1:04d}.png"
        glow_img.save(os.path.join(THEME_DIR, frame_name))
        
        # Also save as animation-*.png for compatibility
        anim_name = f"animation-{frame+1:04d}.png"
        glow_img.save(os.path.join(THEME_DIR, anim_name))

    print(f"[+] Generated {num_frames} throbber & animation frames.")

def draw_auxiliary_assets():
    # Bullet (for password dots)
    bullet = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    d = ImageDraw.Draw(bullet)
    d.ellipse([(4, 4), (11, 11)], fill=(255, 255, 255, 255))
    bullet.save(os.path.join(THEME_DIR, "bullet.png"))

    # Entry (input box)
    entry = Image.new("RGBA", (280, 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(entry)
    d.rectangle([(2, 2), (277, 37)], outline=(255, 255, 255, 200), width=1)
    d.line([(0, 0), (8, 0)], fill=(255, 255, 255, 255), width=2)
    d.line([(0, 0), (0, 8)], fill=(255, 255, 255, 255), width=2)
    d.line([(279, 0), (271, 0)], fill=(255, 255, 255, 255), width=2)
    d.line([(279, 0), (279, 8)], fill=(255, 255, 255, 255), width=2)
    d.line([(0, 39), (8, 39)], fill=(255, 255, 255, 255), width=2)
    d.line([(0, 39), (0, 31)], fill=(255, 255, 255, 255), width=2)
    d.line([(279, 39), (271, 39)], fill=(255, 255, 255, 255), width=2)
    d.line([(279, 39), (279, 31)], fill=(255, 255, 255, 255), width=2)
    entry.save(os.path.join(THEME_DIR, "entry.png"))

    # Lock icon
    lock = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
    d = ImageDraw.Draw(lock)
    d.arc([(10, 4), (22, 16)], start=180, end=0, fill=(255, 255, 255, 220), width=2)
    d.line([(10, 10), (10, 16)], fill=(255, 255, 255, 220), width=2)
    d.line([(22, 10), (22, 16)], fill=(255, 255, 255, 220), width=2)
    d.rectangle([(8, 16), (24, 28)], outline=(255, 255, 255, 255), width=1)
    d.line([(16, 20), (16, 24)], fill=(255, 255, 255, 255), width=2)
    lock.save(os.path.join(THEME_DIR, "lock.png"))

    print("[+] Auxiliary UI assets generated.")

if __name__ == "__main__":
    draw_watermark()
    draw_throbber_frames()
    draw_auxiliary_assets()
