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
from django.core.mail import send_mail, EmailMessage
import smtplib
from email.mime.text import MIMEText
from PIL import Image
from resizeimage import resizeimage
import pyqrcode
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def save_pdf_ticket(data):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(595, 842))
    can.translate(0, 842)
    can.setFontSize(7)
    can.drawString(191, -188, data['title'])
    can.drawString(191, -212, data['date'])
    can.drawString(321, -212, data['time'])
    can.drawString(200, -234, data['address'])
    can.drawString(205, -259, data['organizer'])
    can.drawString(414, -220, data['type'])
    can.setFontSize(9)
    can.drawString(442, -188, data['order_no'])

    try:
        img_byte = BytesIO()
        photo = data['photo']
        photo.seek(0)
        img_byte.write(photo.read())
        img = Image.open(img_byte)
        img = resizeimage.resize_contain(img, [90, 40])
        img = img.convert('RGB')
        thumb_io = BytesIO()
        img.save(
            thumb_io,
            "JPEG"
        )
        img = ImageReader(thumb_io)
        can.drawImage(img, 411, -270)
    except:
        pass

    qr_byte = BytesIO()
    big_code = pyqrcode.create(data['order_no'])
    big_code.png(qr_byte, scale=6, quiet_zone=0, background=(255, 255, 255, 0))
    img = ImageReader(qr_byte)
    can.drawImage(img, 107, -245, 50, 50)
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # read your existing PDF
    existing_pdf = PdfFileReader(open(os.path.join(
        settings.BASE_DIR, 'ticketing', 'ticket.pdf'), "rb"))
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

 
# def send_out_invitation(subject, receiver, data):
#     sender_email_template = render_to_string(
#         "ticketing/email_template/ticket_email.html", {'ticket_image': data['ticket_image']})
#     mail = EmailMessage(subject, sender_email_template, 'info@eventstracer.com',
#                         receiver)
#     mail.attach_file(data['invitation']); mail.content_subtype = "html"
#     mail.send()


def send_out_invitation(subject, receiver, data):
    event = data['event']
    invitation = data['invitation']
    sender_email_template = render_to_string("ticketing/email_template/ticket_email.html", {'event':event})
    mail = EmailMessage(subject, sender_email_template, 'info@eventstracer.com', receiver)
    mail.attach_file(invitation.ticket.path)
    mail.content_subtype = "html"
    mail.send()
