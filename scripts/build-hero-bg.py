"""
Generate the hero background plate: public/hero-bg.webp

Procedural rather than photographic, and that is the right call for this job
rather than a limitation. The brief asks for architecture that is "heavily
darkened", "low visual contrast behind the text" and "cinematic but
understated" — a real photograph fights the foreground UI at those settings,
because its mid-tones and edge detail survive darkening. A drawn silhouette
degrades gracefully: it is already flat, so pushing it dark leaves shape and
atmosphere without texture noise competing with the headline.

Composition follows the reference: nothing but environment, with the tall
massing pushed to the centre-right so the left third stays clean under
"Master the SAT. / Build skills beyond it."

Re-run with:  python3 scripts/build-hero-bg.py
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import random

PLATES = [
    # (width, height, output, tower scale)
    # Landscape for desktop/tablet, and a genuine portrait plate for phones.
    # A phone hero is very tall and narrow, so `cover` on the landscape plate
    # blows it up into a thin strip of near-empty sky whatever the position is
    # set to. Drawing the composition at portrait dimensions is the only way
    # the architecture actually survives there.
    (2560, 1440, "public/hero-bg.webp", 1.0),
    (1200, 2000, "public/hero-bg-portrait.webp", 1.9),
]

# Deterministic: the same source always produces the same plate, so a rebuild
# never silently changes the site's look.



def build(W, H, OUT, TSCALE):
    random.seed(20260813)
    def lerp(a, b, t):
        return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


    # --------------------------------------------------------------------------
    # 1. Sky. Deep navy overhead easing to a slightly warmer indigo at the horizon,
    #    which is what gives the scene depth without any light source being drawn.
    # --------------------------------------------------------------------------
    TOP = (5, 8, 20)
    HORIZON = (23, 30, 62)

    sky = Image.new("RGB", (W, H), TOP)
    d = ImageDraw.Draw(sky)
    for y in range(H):
        t = (y / H) ** 1.35
        d.line([(0, y), (W, y)], fill=lerp(TOP, HORIZON, t))

    # --------------------------------------------------------------------------
    # 2. Atmospheric glow, centre-right. Drawn on its own layer and screened in, so
    #    it reads as haze in the air rather than as a gradient sitting on the sky.
    # --------------------------------------------------------------------------
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy, r = int(W * 0.62), int(H * 0.66), int(W * 0.42)
    for i in range(60, 0, -1):
        t = i / 60
        rad = int(r * t)
        c = lerp((0, 0, 0), (46, 58, 128), (1 - t) ** 2)
        gd.ellipse([cx - rad, cy - int(rad * 0.72), cx + rad, cy + int(rad * 0.72)], fill=c)
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    sky = Image.blend(sky, Image.new("RGB", (W, H), (0, 0, 0)), 0.0)
    sky = Image.merge(
        "RGB",
        [
            Image.fromarray(
                (
                    255
                    - (255 - __import__("numpy").asarray(sky.split()[i], dtype="int16"))
                    * (255 - __import__("numpy").asarray(glow.split()[i], dtype="int16"))
                    // 255
                ).astype("uint8")
            )
            for i in range(3)
        ],
    )

    base = sky


    def gothic_tower(draw, x, w, top_y, base_y, fill, spire=True, window_fill=None):
        """One tower: body, optional spire, and a column of lancet windows."""
        draw.rectangle([x, top_y, x + w, base_y], fill=fill)
        if spire:
            draw.polygon(
                [(x - w * 0.10, top_y), (x + w / 2, top_y - w * 1.65), (x + w * 1.10, top_y)],
                fill=fill,
            )
        if window_fill:
            # Lancet windows — a rectangle capped with a pointed arch, which is the
            # single shape that reads as "Gothic" at this scale.
            cols = max(1, int(w // 46))
            for c in range(cols):
                wx = x + w * (c + 0.5) / cols - w * 0.10
                ww = max(7, w * 0.16)
                for row in range(3):
                    wy = top_y + w * 0.55 + row * w * 0.62
                    if wy + ww * 2.1 > base_y:
                        break
                    draw.rectangle([wx, wy + ww * 0.75, wx + ww, wy + ww * 2.1], fill=window_fill)
                    draw.polygon(
                        [(wx, wy + ww * 0.78), (wx + ww / 2, wy), (wx + ww, wy + ww * 0.78)],
                        fill=window_fill,
                    )


    def skyline(colour, window_colour, y_base, scale, seed, blur):
        """One depth plane of buildings, drawn then blurred to sit back in the haze."""
        rnd = random.Random(seed)
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        dr = ImageDraw.Draw(layer)
        x = -120
        while x < W + 120:
            w = rnd.randint(int(90 * scale * TSCALE), int(210 * scale * TSCALE))
            h = rnd.randint(int(200 * scale * TSCALE), int(430 * scale * TSCALE))
            # Centre-right gets the tall massing, matching the reference.
            if 0.42 < (x / W) < 0.88:
                h = int(h * rnd.uniform(1.35, 1.95))
            top = y_base - h
            gothic_tower(
                dr,
                x,
                w,
                top,
                y_base,
                colour,
                spire=rnd.random() < 0.55,
                window_fill=window_colour if rnd.random() < 0.8 else None,
            )
            x += w + rnd.randint(int(18 * scale), int(70 * scale))
        if blur:
            layer = layer.filter(ImageFilter.GaussianBlur(blur))
        return layer


    # --------------------------------------------------------------------------
    # 3. Three depth planes. Far ones are lighter and blurrier — aerial perspective
    #    does the work of making it feel deep, so no detail has to be added up close
    #    where it would compete with the UI.
    # --------------------------------------------------------------------------
    base = base.convert("RGBA")
    base.alpha_composite(skyline((26, 33, 68, 255), (52, 66, 130, 34), int(H * 0.88), 0.75, 11, 7))
    base.alpha_composite(skyline((16, 21, 48, 255), (58, 74, 148, 38), int(H * 0.95), 1.05, 22, 3.5))
    base.alpha_composite(skyline((8, 11, 28, 255), (64, 82, 160, 42), int(H * 1.03), 1.45, 33, 1.2))
    base = base.convert("RGB")

    # --------------------------------------------------------------------------
    # 4. Haze drifting across the lower third, tying the planes together.
    # --------------------------------------------------------------------------
    haze = Image.new("RGB", (W, H), (0, 0, 0))
    hd = ImageDraw.Draw(haze)
    for i in range(9):
        y = int(H * (0.58 + i * 0.05))
        hd.ellipse(
            [-W * 0.2, y, W * 1.2, y + random.randint(90, 190)],
            fill=lerp((0, 0, 0), (30, 40, 88), 0.55),
        )
    haze = haze.filter(ImageFilter.GaussianBlur(120))
    base = Image.blend(base, Image.new("RGB", (W, H), (255, 255, 255)), 0.0)
    base = Image.composite(base, base, Image.new("L", (W, H), 255))
    import numpy as np  # noqa: E402  (only needed for the screen blends)

    arr = np.asarray(base, dtype="int16")
    hz = np.asarray(haze, dtype="int16")
    base = Image.fromarray((255 - (255 - arr) * (255 - hz) // 255).astype("uint8"))

    # --------------------------------------------------------------------------
    # 5. Left-side darkening and a vignette. This is part of the plate, not the CSS
    #    overlay: baking it in means the headline sits on genuinely dark pixels even
    #    before the overlay is applied, so the overlay can stay light enough to keep
    #    the architecture visible.
    # --------------------------------------------------------------------------
    shade = Image.new("L", (W, H), 255)
    sd = ImageDraw.Draw(shade)
    for x in range(W):
        t = x / W
        # Full strength at the left edge, gone by ~55% across.
        v = 255 - int(150 * max(0.0, 1.0 - (t / 0.55)) ** 1.25)
        sd.line([(x, 0), (x, H)], fill=v)
    shade = shade.filter(ImageFilter.GaussianBlur(60))

    vig = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vig)
    vd.ellipse([-W * 0.28, -H * 0.42, W * 1.28, H * 1.42], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(260))

    arr = np.asarray(base, dtype="float32")
    arr *= (np.asarray(shade, dtype="float32") / 255.0)[:, :, None]
    arr *= (0.70 + 0.30 * np.asarray(vig, dtype="float32") / 255.0)[:, :, None]

    # Global level pass. The brief wants this heavily darkened and low-contrast —
    # but the CSS navy overlay darkens it AGAIN on top, so the plate has to be left
    # bright enough to survive that second pass. Tuned so the architecture is still
    # legible after the overlay rather than collapsing to black.
    arr = arr * 1.28
    mean = arr.mean()
    arr = (arr - mean) * 0.74 + mean * 0.95

    base = Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))
    base = base.filter(ImageFilter.GaussianBlur(0.6))

    base.save(OUT, "WEBP", quality=86, method=6)

    peak = np.asarray(base).max()
    left = np.asarray(base)[:, : W // 3].mean()
    print(f"wrote {OUT}  {W}x{H}")
    print(f"  mean luminance {np.asarray(base).mean():.1f}/255   peak {peak}")
    print(f"  left-third mean {left:.1f}/255 (headline area — wants to be low)")


for _w, _h, _out, _ts in PLATES:
    build(_w, _h, _out, _ts)
