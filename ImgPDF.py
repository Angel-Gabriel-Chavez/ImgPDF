from fpdf import FPDF # pdf
from PIL import Image # image size
import os # path

pdf = FPDF()

# format of directory paths with images
path = input('Path: ').replace('\\', '/')
imagelist = [path + '/' + i for i in os.listdir(path)]

# set name
name = input('Resulting file name: ')
filepath = path + '/' + name + '.pdf'

# set margin
margin = int(input('Margin: '))

for image in imagelist:

    # ger image size
    cover = Image.open(image)
    width, height = cover.size

    # adjust page size based on image size
    pdf.add_page(format  = (width + (margin * 2),
                            height + (margin * 2))
                 )
    pdf.image(image, margin, margin, width, height)

pdf.output(filepath, 'F')
