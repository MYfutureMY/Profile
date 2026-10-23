#!/bin/sh
# Usage: render_illustrations.sh OUTDIR  -> OUTDIR/*.png (1200x900, transparent corners)
set -e
OUT=$1; HERE=$(dirname "$0")
python3 "$HERE/make_illustrations.py" "$OUT"
CHROME=${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}
for f in "$OUT"/*.svg; do
  n=${f%.svg}
  printf '<html><body style="margin:0;background:transparent">%s</body></html>' "$(cat "$f")" > "$n.html"
  "$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --default-background-color=00000000 \
    --force-device-scale-factor=2 --window-size=600,700 --screenshot="$n.full.png" "file://$n.html" >/dev/null 2>&1
  python3 -c "import sys;from PIL import Image;Image.open(sys.argv[1]).crop((0,0,1200,900)).save(sys.argv[2])" "$n.full.png" "$n.png"
  rm -f "$n.full.png" "$n.html"
done
