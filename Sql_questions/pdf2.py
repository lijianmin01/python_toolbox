from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image


def jpg_to_pdf(jpg, pdf_path):
    (w, h) = Image.open(jpg).size
    user = canvas.Canvas(pdf_path, pagesize=portrait((w, h)))
    user.drawImage(jpg, 0, 0, w, h)
    user.showPage()
    user.save()


if __name__ == '__main__':
    jpg_path = '66.jpg'
    pdf_path = 'code1.pdf'
    jpg_to_pdf(jpg_path, pdf_path)