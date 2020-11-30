# Dateigrößenberechnung bei TIFF-Dateien
# Erstellt: 28/11/20

import enum

class TIFFFormat(enum.Enum):
    Bilevel = 1
    Grayscale = 2
    Palette = 3
    RGB = 4

def calcTiffSize(res):
    points = res[0] * res[1]
    dicSize = {}
    for format in TIFFFormat.__members__.keys():
        if format == "Bilevel":
            size = points * 1
        elif format == "Grayscale":
            size = points * 8
        elif format == "RGB":
            size = points * 24
        else:
            size = points * 8
        dicSize[format] = round(size / 8 / 1048576,2)

    return dicSize

# res = (1920,1080)
res = (640,480)
sizeDic = calcTiffSize(res)
for format in sizeDic:
    print(f"Im {format}-Format belegt das Bild {sizeDic[format]} MB")
