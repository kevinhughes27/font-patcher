#!/usr/bin/env python3
# apt-get install python3-fontforge

import fontforge
import psMat
import pathlib

for f in pathlib.Path("./src_fonts").glob("*"):
    font = fontforge.open(str(f))
    font_height = font.os2_windescent + font.os2_winascent

    # centered reference char?
    side = 0xe0b0  # 

    separators = [
        0xe0ba,  # 

        0xe0bc,  # 

        0xe0b8,  # 

        0xe0be,  # 
    ]

    scale = psMat.scale(0.5, 1)
    translate = psMat.translate(0, -48)

    for sep in separators:
        font[sep].transform(scale)
        font[sep].transform(translate)

    # lsep 
    # needs to be moved down
    # sep = 0xe0b8
    # translate = psMat.translate(-1, -12)
    # font[sep].foreground = font[sep].foreground.transform(translate)

    # lsep2 
    # needs to be moved up
    # sep = 0xe0be
    # translate = psMat.translate(1, 12)
    # font[sep].foreground = font[sep].foreground.transform(translate)

    # rsep 
    # needs to be moved up
    # sep = 0xe0ba
    # translate = psMat.translate(1, 12)
    # font[sep].foreground = font[sep].foreground.transform(translate)

    # for sep in separators:
    #     print(font[sep].foreground.boundingBox())
    #
    # breakpoint()

    font.generate(f"./fonts/{f.name}", flags=(str('opentype')))

# echo test:
# echo -e "\ue0be\e[1;42m BG \e[0m\ue0b8"
