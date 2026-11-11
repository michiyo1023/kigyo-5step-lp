# 龍体文字帳（蛇腹）PDF作成スクリプト
# 使い方: python3 make_book.py  → ryutai_book.pdf ができる
# images/あ.png ... があれば円の中に入る。なければ点線の空き円になる。
# texts.csv の「説明」列に、各音の説明文を入れる。
import csv, os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

HERE = os.path.dirname(os.path.abspath(__file__))
PW, PH = 55*mm, 90*mm          # 1ページの大きさ
PER_STRIP = 5                  # 1本の帯に何ページ
STRIPS = 2                     # A4 1枚に何本
CIRCLE_D = 38*mm

def pick_font():
    for p in ["/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf",
              "/usr/share/fonts/truetype/ipafont-gothic/ipag.ttf"]:
        if os.path.exists(p):
            pdfmetrics.registerFont(TTFont("JP", p)); return "JP"
    pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5")); return "HeiseiKakuGo-W5"
FONT = pick_font()

def wrap(text, width_mm, size):
    per = max(1, int(width_mm*mm // size))
    out = []
    for para in text.split("\n"):
        out += [para[i:i+per] for i in range(0, len(para), per)] or [""]
    return out

def load_rows():
    path = os.path.join(HERE, "texts.csv")
    with open(path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def draw_panel(c, x, y, row):
    kana, text = row["音"], row.get("説明", "")
    cx, cy = x + PW/2, y + PH - 6*mm - CIRCLE_D/2
    img = next((os.path.join(HERE, "images", kana + e) for e in (".png", ".jpg", ".jpeg")
                if os.path.exists(os.path.join(HERE, "images", kana + e))), None)
    c.setLineWidth(0.6)
    if img:
        c.setStrokeColorRGB(.45, .55, .8); c.circle(cx, cy, CIRCLE_D/2)
        pad = 4*mm; s = CIRCLE_D - 2*pad
        c.drawImage(img, cx - s/2, cy - s/2, s, s, preserveAspectRatio=True, mask="auto")
    else:
        c.setStrokeColorRGB(.7, .7, .7); c.setDash(2, 2); c.circle(cx, cy, CIRCLE_D/2); c.setDash()
    c.setFillColorRGB(0, 0, 0); c.setFont(FONT, 20)
    c.drawCentredString(cx, y + PH - 6*mm - CIRCLE_D - 11*mm, kana)
    c.setFont(FONT, 6.5)
    ty = y + PH - 6*mm - CIRCLE_D - 18*mm
    for line in wrap(text, 55-10, 6.5):
        c.drawString(x + 5*mm, ty, line); ty -= 9

def main():
    rows = load_rows()
    c = canvas.Canvas(os.path.join(HERE, "ryutai_book.pdf"), pagesize=landscape(A4))
    W, H = landscape(A4)
    ox = (W - PW*PER_STRIP)/2
    gap = (H - PH*STRIPS)/(STRIPS+1)
    per_sheet = PER_STRIP*STRIPS
    for s in range(0, len(rows), per_sheet):
        for i, row in enumerate(rows[s:s+per_sheet]):
            strip, col = divmod(i, PER_STRIP)
            x = ox + col*PW
            y = H - gap*(strip+1) - PH*(strip+1)
            draw_panel(c, x, y, row)
            # 折り線（薄い点線）と外枠
            c.setStrokeColorRGB(.8, .8, .8); c.setLineWidth(.3); c.setDash(1, 2)
            c.rect(x, y, PW, PH); c.setDash()
        c.showPage()
    c.save()
    print("できました:", os.path.join(HERE, "ryutai_book.pdf"), f"({len(rows)}ページ分)")
main()
