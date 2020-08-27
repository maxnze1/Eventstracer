from django.shortcuts import render, redirect, reverse
from formtools.wizard.views import SessionWizardView
from registrations.forms import (
    SMERegistration1,
    SMERegistration2,
    SMERegistration3,
    SMERegistration4,
    SMERegistrationPayment
)
from registrations.models import SMERegistration
from uuid import uuid4
from registrations import utils
from django.conf import settings
import smtplib
import os
from email.mime.text import MIMEText
from django.core.files.storage import FileSystemStorage

# Create your views here.


FORMS = [("SME1", SMERegistration1),
         ("SME2", SMERegistration2),
         ("SME3", SMERegistration3),
         ("SME4", SMERegistration4),
         ("SME5", SMERegistrationPayment)
         ]

TEMPLATES = {"SME1": "sme1-form.html",
             "SME2": "sme2-form.html",
             "SME3": "sme3-form.html",
             "SME4": "sme4-form.html",
             "SME5": "sme-payment.html"
             }


class SMERegistrationWizard(SessionWizardView):
    form_list = FORMS
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'documents'))

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context = super(SMERegistrationWizard, self).get_context_data(
            form=form, **kwargs)
        phone = self.get_all_cleaned_data().get('phone_number')
        email = self.get_all_cleaned_data().get('email')
        reference = str(uuid4().int >> 100)
        context.update(
            {'phone': phone, 'email': email, 'reference': reference})
        return context

    def done(self, form_list, **kwargs):
        for i, form in enumerate(form_list):
            if i == 0:
                first = form.cleaned_data
            elif i == 1:
                second = form.cleaned_data
            elif i == 2:
                third = form.cleaned_data
            elif i == 4:
                last = form.cleaned_data
        user = None if not self.request.user.is_authenticated else self.request.user
        reg_obj = SMERegistration(circuit=first['circuit'],  company_name=first['company_name'], type_of_business=first['type_of_business'],
                                  email=first['email'], payment_reference=last['reference'],
                                  company_address=first['company_sector'], company_sector=first['company_sector'],
                                  years_business=first['years_business'], contact_person=first['contact_person'],
                                  company_person_designation=first['company_person_designation'],
                                  phone_number=first['phone_number'],
                                  description=second['description'], website=second['website'],
                                  date_incorporation=second['date_incorporation'],
                                  contact_person2=second['contact_person'], employed_person=second['employed_person'],
                                  annual_revenue=second['annual_revenue'], supporting_document=first['supporting_document'],
                                  business_projection=third['business_projection'],
                                  challenges=third['challenges'], outlets=third['outlets'],
                                  improve_business=third['improve_business'], photo=third['photo'], user=user)

        get_status_payment = utils.verify_transaction(str(last['reference']))
        if get_status_payment:
            reg_obj.payment = 'S'
            subject = "Silverbird SME Registration"
            utils.send_out_invitation(
                subject, [first['email']], first['company_name'])
        else:
            reg_obj.payment = 'U'

        subject = "Silverbird SME Registration"
        utils.send_out_invitation(
            subject, [first['email']], first['company_name'])
        reg_obj.save()
        return render(self.request, 'thank-you.html')
