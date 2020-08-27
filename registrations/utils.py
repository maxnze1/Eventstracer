from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame, KeepInFrame
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet
import os
import requests
import json
from registrations import models
from django.conf import settings
from django.core.mail import send_mail
import smtplib
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from PIL import Image
from resizeimage import resizeimage


def save_pdf(data):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(595, 842))
    can.translate(0, 842)
    can.drawString(246, -245, data['company_name'])
    can.drawString(246, -288, data['biz_sector'])
    can.drawString(246, -327, data['contact1'])
    can.drawString(246, -371, data['contact_designation'])
    can.drawString(59, -480, data['phone'])
    can.drawString(59, -535, data['NOE'])
    can.drawString(59, -432, data['biz_years'])
    #can.drawString(334, -430, data['doi'])
    can.drawString(334, -484, data['annual_revenue'])

    styles = getSampleStyleSheet()
    biz_improve = [Paragraph(data['biz_improve'], styles['Normal'])]
    biz_improve_inframe = KeepInFrame(215, 70, biz_improve)
    biz_improve_frame = Frame(320, -655, 215, 70)
    biz_improve_frame.addFromList([biz_improve_inframe], can)

    address = [Paragraph(data['company_address'], styles['Normal'])]
    address_inframe = KeepInFrame(215, 70, address)
    address_frame = Frame(51, -655, 215, 70)
    address_frame.addFromList([address_inframe], can)

    can.setFont("Helvetica-Bold", 25)
    can.setFillColor("blue")
    can.drawString(171, -750, data['score'])

    img_byte = BytesIO()
    photo = data['photo']
    photo.seek(0)
    img_byte.write(photo.read())
    img = Image.open(img_byte)
    img = resizeimage.resize_contain(img, [172, 182])
    img = img.convert('RGB')
    thumb_io = BytesIO()
    img.save(
        thumb_io,
        "JPEG"
    )
    img = ImageReader(thumb_io)
    can.drawImage(img, 51, -389)

    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # read your existing PDF
    existing_pdf = PdfFileReader(open(os.path.join(
        settings.BASE_DIR, 'registrations', 'circuit_registration_form.pdf'), "rb"))
    output = PdfFileWriter()

    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)
    output.addPage(page)

    packet2 = BytesIO()
    packet2.seek(0)
    output.write(packet2)

    return packet2


def verify_transaction(reference):
    try:
        response = requests.get("https://api.paystack.co/transaction/verify/{}".format(reference),
                                headers={"Authorization": "Bearer {}".format(settings.PAYSTACK_SECRET_KEY)})
        print(type(response.status_code), "type")
        if response.status_code == 200:
            get_data = json.loads(response.content)
            if get_data['status'] == True:
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print("error", e)
        return False


def send_out_invitation(subject, receiver, data):
    print(receiver, "\n\n\n", subject, data, "here")
    sender_email_template = render_to_string(
        "email_template/sme_email.html", {'Eventstracer': data})
    send_mail(subject, strip_tags(sender_email_template), 'info@eventstracer.com',
              receiver, html_message=sender_email_template)
