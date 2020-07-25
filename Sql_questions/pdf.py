from fpdf import FPDF
from PIL import Image
import os

def makePdf(pdfFileName, listPages):

	cover = Image.open(listPages[0])
	width, height = cover.size

	pdf = FPDF(unit = "pt", format = [width, height])

	for page in listPages:
		pdf.add_page()
		pdf.image(page, 0, 0)

	pdf.output(pdfFileName, "F")


path = 'data2'

imgFiles=[]
for root, dirs, files in os.walk(path, topdown=True):
	for img_file in files:
		img_path = root + '\\' + img_file
		imgFiles.append(img_path)

makePdf("result.pdf", imgFiles)