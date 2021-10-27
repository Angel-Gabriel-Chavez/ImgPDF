from fpdf import FPDF # pdf
from PIL import Image # image size
import os # path

pdf = FPDF()

# format of directory paths with images
path = input('path: ').replace('\\', '/')
imagelist = [path + '/' + i for i in os.listdir(path)]

# set margin
margin = int(input('margin: '))

for image in imagelist:

    # ger image size
    cover = Image.open(image)
    width, height = cover.size

    # adjust page size based on image size
    pdf.add_page(format  = (width + (margin * 2),
                            height + (margin * 2))
                 )
    pdf.image(image, margin, margin, width, height)

pdf.output(path + '/yourfile.pdf', 'F')
