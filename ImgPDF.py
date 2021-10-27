from fpdf import FPDF
from PIL import Image
import os

pdf = FPDF()
path = 'C:/Users/BatmanDorado/Desktop/PixelArt'
imagelist = [path + '/' + i for i in os.listdir(path)]

margin = 10

for image in imagelist:
    cover = Image.open(image)
    width, height = cover.size
    pdf.add_page(format  = (width + (margin * 2),
                            height + (margin * 2))
                 )
    pdf.image(image, margin, margin, width, height)

pdf.output("C:/Users/BatmanDorado/Desktop/PixelArt/yourfile.pdf", "F")
