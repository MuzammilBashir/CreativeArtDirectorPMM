"""Score a Cube Blast restyle against the style reference (colour, highlights, exposure) and the
gameplay source (geometry). Usage: python score.py candidate.png [x0 y0 x1 y1]  (board bounds, 7x8 grid)."""
import sys, colorsys
import numpy as np
from PIL import Image

REF = "../../references/2.png"
SRC = "../../references/block-gameplay-source.webp"
SRC_BOARD = (105, 370, 805, 1150)
REF_BOARD = (118, 348, 855, 1105)  # 9x9 cube grid in the style reference


def load(p):
    return np.asarray(Image.open(p).convert("RGB")).astype(float) / 255


def hsv(px):
    return np.array([colorsys.rgb_to_hsv(*c) for c in px])


def family(h, s, v):
    if v < 0.32: return "empty"
    if s < 0.22 and v > 0.7: return "white"
    d = h * 360
    if d < 12 or d > 340: return "red"
    if d < 38: return "orange"
    if d < 68: return "yellow"
    if d < 165: return "green"
    if d < 218: return "blue"
    if d < 250: return "navy"
    return "purple"


def lab(rgb):
    c = np.where(rgb > 0.04045, ((rgb + 0.055) / 1.055) ** 2.4, rgb / 12.92)
    xyz = c @ np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]]).T
    xyz /= [0.9505, 1.0, 1.089]
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def board_stats(img, box):
    x0, y0, x1, y1 = box
    px = img[y0:y1:3, x0:x1:3].reshape(-1, 3)
    hv = hsv(px)
    fams = np.array([family(*c) for c in hv])
    med = {f: np.median(px[fams == f], 0) for f in set(fams) if (fams == f).sum() > 200}
    solid = fams != "empty"
    highlight = ((hv[:, 2] > 0.93) & (hv[:, 1] < 0.3) & (fams != "white")).mean()
    return med, hv[solid, 2].mean(), hv[solid, 1].mean(), highlight


def grid(img, box, cols=7, rows=8):
    x0, y0, x1, y1 = box
    cw, ch = (x1 - x0) / cols, (y1 - y0) / rows
    out = []
    for r in range(rows):
        for c in range(cols):
            cx, cy = int(x0 + (c + .5) * cw), int(y0 + (r + .5) * ch)
            patch = img[cy - int(ch * .15):cy + int(ch * .15), cx - int(cw * .15):cx + int(cw * .15)].reshape(-1, 3)
            out.append(lab(np.median(patch, 0)))
    return np.array(out)


def partition_agreement(a, b, tol=14):
    # palettes differ between images, so compare which cells share a colour rather than the colours
    sa = np.linalg.norm(a[:, None] - a[None], axis=-1) < tol
    sb = np.linalg.norm(b[:, None] - b[None], axis=-1) < tol
    iu = np.triu_indices(len(a), 1)
    bad = np.where((sa != sb).sum(1) > len(a) * 0.1)[0]
    return (sa[iu] == sb[iu]).mean(), bad


def main():
    cand = load(sys.argv[1])
    box = tuple(map(int, sys.argv[2:6])) if len(sys.argv) > 5 else None
    ref, src = load(REF), load(SRC)
    rmed, rv, rs, rh = board_stats(ref, REF_BOARD)
    cmed, cv, cs, ch = board_stats(cand, box)

    shared = [f for f in ("red", "yellow", "green", "blue") if f in rmed]
    # orange restyle blocks are compared to the reference's yellow-orange if no orange exists there
    pairs = [(f, f) for f in shared if f in cmed]
    if "orange" in cmed and "orange" not in rmed and "yellow" in rmed and "yellow" not in cmed:
        pairs.append(("orange", "yellow"))
    des = {c: float(np.linalg.norm(lab(cmed[c]) - lab(rmed[r]))) for c, r in pairs}
    de = np.mean(list(des.values()))
    colour = 40 * max(0, 1 - de / 30)
    exposure = 20 * max(0, 1 - abs(cv - rv) / 0.15) * 0.6 + 20 * max(0, 1 - abs(cs - rs) / 0.25) * 0.4
    hl = 15 * max(0, 1 - abs(ch - rh) / max(rh, 0.01))
    g_src, g_c = grid(src, SRC_BOARD), grid(cand, box)
    geo_match, bad = partition_agreement(g_src, g_c)
    geometry = 25 * max(0, (geo_match - 0.8) / 0.2)
    total = colour + exposure + hl + geometry

    hexs = lambda c: "#%02x%02x%02x" % tuple(int(x * 255) for x in c)
    print("colour dE per family:", {k: round(v, 1) for k, v in des.items()})
    print("ref colours :", {k: hexs(v) for k, v in rmed.items()})
    print("cand colours:", {k: hexs(v) for k, v in cmed.items()})
    print(f"brightness ref {rv:.2f} cand {cv:.2f} | saturation ref {rs:.2f} cand {cs:.2f}")
    print(f"highlight coverage ref {rh:.3f} cand {ch:.3f}")
    print(f"geometry pair agreement {geo_match:.3f}; suspect cells (row,col):", [(i // 7 + 1, i % 7 + 1) for i in bad])
    print(f"SCORE colour {colour:.1f}/40 exposure {exposure:.1f}/20 highlights {hl:.1f}/15 "
          f"geometry {geometry:.1f}/25 = {total:.1f}/100")


if __name__ == "__main__":
    main()
