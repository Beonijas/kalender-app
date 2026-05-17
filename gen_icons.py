from PIL import Image, ImageDraw, ImageFont
import os, math

def draw_icon(size):
    img = Image.new('RGBA', (size, size), (0,0,0,0))
    d = ImageDraw.Draw(img)
    r = size * 0.18
    d.rounded_rectangle([0,0,size-1,size-1], radius=r, fill='#1a1a2e')
    cx, cy = size/2, size/2
    # Moon crescent
    moon_r = size * 0.28
    d.ellipse([cx-moon_r, cy-moon_r-size*0.02, cx+moon_r, cy+moon_r-size*0.02], fill='#e8c87a')
    d.ellipse([cx+moon_r*0.25-size*0.01, cy-moon_r-size*0.02, cx+moon_r*0.25+moon_r*0.85, cy+moon_r*0.7-size*0.02], fill='#1a1a2e')
    # Stars
    for sx, sy, sr in [(0.22,0.22,0.025),(0.78,0.25,0.018),(0.15,0.6,0.015),(0.82,0.65,0.02),(0.5,0.12,0.016)]:
        d.ellipse([size*sx-size*sr, size*sy-size*sr, size*sx+size*sr, size*sy+size*sr], fill='#ffffff')
    # Calendar grid dots at bottom
    dot_y = size*0.78
    for i in range(5):
        dx = size*0.25 + i*size*0.13
        d.ellipse([dx-size*0.018, dot_y-size*0.018, dx+size*0.018, dot_y+size*0.018], fill='#5b8dee')
    return img

for sz in [192, 512, 180, 152, 120]:
    img = draw_icon(sz)
    img.save(f'/home/claude/kalender-pwa/icons/icon-{sz}.png')
    print(f'Generated {sz}x{sz}')

# Apple touch icon
img180 = draw_icon(180)
img180.save('/home/claude/kalender-pwa/icons/apple-touch-icon.png')
print("Done")
