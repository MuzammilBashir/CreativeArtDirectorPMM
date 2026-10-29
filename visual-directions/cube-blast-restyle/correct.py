"""Shift each block colour family on the board to the reference's measured tone, keeping shading.
Usage: python correct.py in.png out.png x0 y0 x1 y1"""
import sys
import numpy as np
from PIL import Image
from score import lab, family, hsv, load  # noqa: E402  (score.py's main() is guarded below)

TARGET = {"red": "#c60c0c", "yellow": "#e4bd05", "green": "#37a00b", "blue": "#2a80d8",
          "navy": "#2c4cc4", "purple": "#7c30c4", "white": "#e6e2d8", "orange": "#e07a0a"}


def lab2rgb(L):
    fy = (L[..., 0] + 16) / 116
    f = np.stack([fy + L[..., 1] / 500, fy, fy - L[..., 2] / 200], -1)
    xyz = np.where(f > 0.2069, f ** 3, (f - 16 / 116) / 7.787) * [0.9505, 1.0, 1.089]
    rgb = xyz @ np.array([[3.2406, -1.5372, -0.4986], [-0.9689, 1.8758, 0.0415], [0.0557, -0.2040, 1.0570]]).T
    rgb = np.clip(rgb, 0, 1)
    return np.where(rgb > 0.0031308, 1.055 * rgb ** (1 / 2.4) - 0.055, 12.92 * rgb)


def main():
    img = load(sys.argv[1])
    x0, y0, x1, y1 = map(int, sys.argv[3:7])
    region = img[y0:y1, x0:x1]
    flat = region.reshape(-1, 3)
    fams = np.array([family(*c) for c in hsv(flat)])
    # orange pieces' light shading reads as "yellow"; keep it with orange so gameplay colours never change
    if (fams == "orange").sum() > (fams == "yellow").sum():
        fams[fams == "yellow"] = "orange"
    L = lab(flat)
    for f, hx in TARGET.items():
        m = fams == f
        if m.sum() < 200:
            continue
        tgt = lab(np.array([int(hx[i:i + 2], 16) / 255 for i in (1, 3, 5)]))
        d = tgt - np.median(L[m], 0)
        if "--hue-only" in sys.argv:  # keep lightness from an earlier tone-curve pass
            d[0] = 0
        L[m] += d
    img[y0:y1, x0:x1] = lab2rgb(L).reshape(region.shape)
    Image.fromarray((img * 255).astype(np.uint8)).save(sys.argv[2])


if __name__ == "__main__":
    main()
