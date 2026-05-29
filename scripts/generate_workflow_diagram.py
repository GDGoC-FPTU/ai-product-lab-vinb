"""Generate 04-workflow-diagram.png for lab submission (current-state workflow)."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "04-workflow-diagram.png"

W, H = 1200, 520
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype("arial.ttf", 16)
    font_b = ImageFont.truetype("arial.ttf", 20)
    font_t = ImageFont.truetype("arial.ttf", 24)
except OSError:
    font = font_b = font_t = ImageFont.load_default()

draw.text((20, 12), "Xanh SM — Current-State: Xu ly su co pin (Handoff & Bottleneck)", fill="black", font=font_t)

boxes = [
    (40, 80, 200, 180, "Buoc 1\nNhan cuoc goi\n2 phut"),
    (260, 80, 420, 180, "Buoc 2\nTra GPS xe\n2 phut\nHandoff"),
    (480, 80, 640, 180, "Buoc 3\nTra tram sac\n5 phut BOTTLENECK"),
    (700, 80, 860, 180, "Buoc 4\nSoan SMS\n5 phut BOTTLENECK"),
    (920, 80, 1080, 180, "Buoc 5\nGoi cuu ho\n1 phut"),
]

for x1, y1, x2, y2, label in boxes:
    color = "#ffcccc" if "BOTTLENECK" in label else "#e8f4fc"
    draw.rectangle([x1, y1, x2, y2], outline="black", width=2, fill=color)
    draw.multiline_text((x1 + 10, y1 + 20), label, fill="black", font=font)

for i in range(len(boxes) - 1):
    x2 = boxes[i][2]
    y_mid = 130
    x1_next = boxes[i + 1][0]
    draw.line([(x2, y_mid), (x1_next, y_mid)], fill="black", width=2)
    draw.polygon([(x1_next - 8, y_mid - 5), (x1_next - 8, y_mid + 5), (x1_next, y_mid)], fill="black")

draw.text((40, 220), "Tong: ~15 phut/luot  |  Do: Den / Handoff giua Dispatcher - Tai xe - He thong tram sac", fill="#333", font=font_b)
draw.text((40, 260), "Legend: BOTTLENECK = buoc 3-4 (tra tram + soan tin)", fill="red", font=font)
draw.text((40, 300), "Vin Smart Future Lab 02 — Current-State Workflow Diagram", fill="#666", font=font)

img.save(OUT)
print(f"Saved {OUT}")
