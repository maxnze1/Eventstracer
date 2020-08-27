from django.test import TestCase

# Create your tests here.

from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO, StringIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame, KeepInFrame
from reportlab.lib.styles import getSampleStyleSheet
import os


packet = BytesIO()
can = canvas.Canvas(packet, pagesize=(595, 842))
can.translate(0, 842)

can.drawImage('dp.jpg', 51, -387)

can.save()

# move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)

# read your existing PDF
existing_pdf = PdfFileReader(
    open('circuit_registration_form.pdf', "rb"))
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page2 = new_pdf.getPage(0)
page.mergePage(page2)
output.addPage(page)

outf = open("save.pdf", 'wb')

output.write(outf)
outf.close()



