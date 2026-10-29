"""Match each block family's lightness distribution (not just its median) to the reference, then the whole board's.
Fixes contrast as well as tone. Usage: python correct2.py in.png out.png x0 y0 x1 y1"""
import sys
import numpy as np
from PIL import Image
from score import lab, family, hsv, load, REF, REF_BOARD
from correct import lab2rgb

# family -> (reference family whose lightness spread it copies, L offset, a/b target hex)
PLAN = {"red": ("red", 0, "#c60c0c"), "yellow": ("yellow", 0, "#e4bd05"), "green": ("green", 0, "#37a00b"),
        "blue": ("blue", 0, "#2a86dc"), "navy": ("blue", -8, "#2c4cc4"), "purple": ("blue", -6, "#8a3cc8"),
        "orange": ("yellow", -8, "#f0880c"),  # source has orange pieces; never recolour gameplay
        }


def fams_of(px):
    f = np.array([family(*c) for c in hsv(px)])
    return f


def qmatch(x, ref):
    # smooth tone curve through 21 quantiles; per-pixel rank matching amplified grain into blotches
    q = np.linspace(0, 100, 21)
    return np.interp(x, np.percentile(x, q), np.percentile(ref, q))


def main():
    img, ref = load(sys.argv[1]), load(REF)
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    rx0, ry0, rx1, ry1 = REF_BOARD
    rpx = ref[ry0:ry1:2, rx0:rx1:2].reshape(-1, 3)
    rL, rf = lab(rpx), fams_of(rpx)
    rf[rf == "navy"] = "blue"  # the reference's "navy" pixels are blue-cube shading
    region = img[y0:y1, x0:x1]
    flat = region.reshape(-1, 3)
    f, L = fams_of(flat), lab(flat)
    for fam, (src, off, hx) in PLAN.items():
        m = f == fam
        if m.sum() < 200:
            continue
        L[m, 0] = qmatch(L[m, 0], rL[rf == src, 0] + off)
        tgt = lab(np.array([int(hx[i:i + 2], 16) / 255 for i in (1, 3, 5)]))
        L[m, 1:] += tgt[1:] - np.median(L[m, 1:], 0)
    w = f == "white"  # no white in the reference: keep its shading, just soften it
    if w.sum() > 200:
        L[w, 0] = 86 + 0.7 * (L[w, 0] - np.median(L[w, 0]))
    # half-strength whole-board match lifts the dark seams/stud crevices toward the reference's shadow level
    L[:, 0] = 0.5 * L[:, 0] + 0.5 * qmatch(L[:, 0], rL[:, 0])
    img[y0:y1, x0:x1] = lab2rgb(L).reshape(region.shape)
    Image.fromarray((img * 255).astype(np.uint8)).save(sys.argv[2])


if __name__ == "__main__":
    main()
