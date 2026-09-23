"""annotate.py: split a panel into a clean image and an annotation layer.

Plan section 3. Colour-saturation split first: author annotations (arrows, boxes, text, markers) are
usually drawn in saturated colour over a greyscale micrograph or a black-on-white plot. Where the
annotation is white or black, saturation cannot see it and we fall back to the stored OCR boxes.

  split(path) -> {clean: PIL, layer_mask: PIL(L), regions: [...], method, coverage, ok}

Never inpaints. The clean image carries the removed region as a flat mask, and the region list is
declared with the item so a grader can check it does not overlap the graded feature.
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SAT_MIN = 90        # HSV S above this is "coloured"
VAL_MIN = 60        # and not near-black
MIN_AREA = 12       # px, drop specks
MAX_COVER = 0.25    # a layer covering more than this is not an annotation layer


def _components(mask, min_area=MIN_AREA):
    """connected components of a boolean mask, as (x0, y0, x1, y1, area), no scipy"""
    h, w = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    out = []
    idx = np.argwhere(mask)
    lookup = set(map(tuple, idx))
    for sy, sx in idx:
        if seen[sy, sx]: continue
        stack = [(sy, sx)]; seen[sy, sx] = True
        x0 = x1 = sx; y0 = y1 = sy; area = 0
        while stack:
            y, x = stack.pop(); area += 1
            if x < x0: x0 = x
            if x > x1: x1 = x
            if y < y0: y0 = y
            if y > y1: y1 = y
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w and not seen[ny, nx] and (ny, nx) in lookup:
                        seen[ny, nx] = True; stack.append((ny, nx))
        if area >= min_area:
            out.append((int(x0), int(y0), int(x1) + 1, int(y1) + 1, int(area)))
    return out


def saturation_mask(im):
    hsv = np.asarray(im.convert('HSV'), dtype=np.int16)
    s, v = hsv[:, :, 1], hsv[:, :, 2]
    return (s >= SAT_MIN) & (v >= VAL_MIN)


def ocr_mask(im, tokens):
    """fallback: the stored OCR boxes, for white or black annotations saturation cannot see"""
    m = np.zeros((im.size[1], im.size[0]), dtype=bool)
    for t in tokens or []:
        b = t.get('box') or t.get('bbox')
        if not b or len(b) != 4: continue
        x0, y0, x1, y1 = [int(round(v)) for v in b]
        x0, y0 = max(0, x0), max(0, y0); x1, y1 = min(im.size[0], x1), min(im.size[1], y1)
        if x1 > x0 and y1 > y0: m[y0:y1, x0:x1] = True
    return m


def split(path, tokens=None, pad=3):
    im = Image.open(path).convert('RGB')
    m = saturation_mask(im); method = 'saturation'
    cover = float(m.mean())
    if cover < 0.0005 or cover > MAX_COVER:
        m2 = ocr_mask(im, tokens)
        if m2.any():
            m, method, cover = m2, 'ocr_boxes', float(m2.mean())
        elif cover > MAX_COVER:
            return {'ok': False, 'method': 'saturation', 'coverage': cover, 'regions': [],
                    'why': f'coloured area {cover:.1%} exceeds {MAX_COVER:.0%}: this is a colour figure, not an annotation layer'}
        else:
            return {'ok': False, 'method': 'none', 'coverage': cover, 'regions': [],
                    'why': 'no saturated pixels and no OCR boxes: nothing to split'}
    regions = _components(m)
    if not regions:
        return {'ok': False, 'method': method, 'coverage': cover, 'regions': [],
                'why': 'mask has no component above the area floor'}
    # grow each region slightly so antialiased edges go with it
    lay = Image.new('L', im.size, 0); d = ImageDraw.Draw(lay)
    for x0, y0, x1, y1, _ in regions:
        d.rectangle([max(0, x0 - pad), max(0, y0 - pad),
                     min(im.size[0], x1 + pad), min(im.size[1], y1 + pad)], fill=255)
    clean = im.copy()
    grey = np.asarray(im.convert('L'))
    fill = int(np.median(grey))                     # flat, visible, declared: not inpainting
    clean.paste(Image.new('RGB', im.size, (fill, fill, fill)), (0, 0), lay)
    overlay = Image.composite(im, Image.new('RGB', im.size, (255, 255, 255)), lay)
    return {'ok': True, 'method': method, 'coverage': cover,
            'regions': [{'box': [x0, y0, x1, y1], 'area': a} for x0, y0, x1, y1, a in regions],
            'clean': clean, 'layer_mask': lay, 'overlay': overlay, 'fill': fill,
            'masked_fraction': float(np.asarray(lay).mean() / 255)}


def overlaps(region_boxes, feature_box):
    if not feature_box: return False
    fx0, fy0, fx1, fy1 = feature_box
    for b in region_boxes:
        x0, y0, x1, y1 = b['box'] if isinstance(b, dict) else b
        if x0 < fx1 and fx0 < x1 and y0 < fy1 and fy0 < y1: return True
    return False


if __name__ == '__main__':
    r = split(sys.argv[1])
    print(json.dumps({k: v for k, v in r.items() if k not in ('clean', 'layer_mask', 'overlay')}, indent=1)[:900])
