"""
Generates a flat-square style SVG badge showing the current time in Pokhara (Asia/Kathmandu).
Run on a schedule via GitHub Actions and commit the output — this is what makes the
badge in the README actually reflect current time, since GitHub caches embedded images
and can't run live JS.
"""
from datetime import datetime
from zoneinfo import ZoneInfo
import os

TZ = ZoneInfo("Asia/Kathmandu")
LABEL = "pokhara"
ACCENT = "#D4703F"
LABEL_BG = "#000000"

OUT_DIR = "readme-assets"
OUT_PATH = os.path.join(OUT_DIR, "pokhara-time.svg")


def build_svg(label: str, value: str, label_bg: str, value_bg: str) -> str:
    # Rough character-based width estimate, flat-square shields.io look
    label_w = 8 * len(label) + 20
    value_w = 8 * len(value) + 20
    total_w = label_w + value_w
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="20">
  <rect width="{label_w}" height="20" fill="{label_bg}"/>
  <rect x="{label_w}" width="{value_w}" height="20" fill="{value_bg}"/>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="{label_w/2}" y="14">{label}</text>
    <text x="{label_w + value_w/2}" y="14">{value}</text>
  </g>
</svg>"""


def main():
    now = datetime.now(TZ)
    value = now.strftime("%I:%M %p").lstrip("0") + " UTC+5:45"
    svg = build_svg(LABEL, value, LABEL_BG, ACCENT)

    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        f.write(svg)

    print(f"Wrote {OUT_PATH} -> {value}")


if __name__ == "__main__":
    main()
