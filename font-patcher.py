#!/usr/bin/env python3
# apt-get install python3-fontforge

import fontforge
import psMat
import pathlib

for f in pathlib.Path("./src_fonts").glob("*"):
    font = fontforge.open(str(f))

    separators = [
        0xe0ba,
        0xe0bc,
        0xe0b8,
        0xe0be,
    ]

    scale = psMat.scale(0.5, 1)
    translate = psMat.translate(0, 10)

    for sep in separators:
        font[sep].foreground = font[sep].foreground.transform(scale)
        font[sep].foreground = font[sep].foreground.transform(translate)

    font.generate(f"./fonts/{f.name}", flags=(str('opentype')))
