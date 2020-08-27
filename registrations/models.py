from django.db import models
from django.core.files.base import ContentFile
from registrations import utils
from django.conf import settings
import os
# Create your models here.


class SMEScore(models.Model):
    limited_liability = models.IntegerField()
    registered_business_name = models.IntegerField()
    partnership = models.IntegerField()
    unregistered = models.IntegerField()
    NYB_less_than_1_year = models.IntegerField()
    NYB_1_to_3_year = models.IntegerField()
    NYB_3_to_5_year = models.IntegerField()
    NYB_over_5_year = models.IntegerField()
    email = models.IntegerField()
    website = models.IntegerField()
    rc_number = models.IntegerField()
    DOI_less_than_1_year = models.IntegerField()
    DOI_1_to_3_year = models.IntegerField()
    DOI_3_to_5_year = models.IntegerField()
    DOI_over_5_year = models.IntegerField()
    NPE_0_to_5_persons = models.IntegerField()
    NPE_5_to_10_persons = models.IntegerField()
    NPE_more_than_10_persons = models.IntegerField()
    AR_0_to_5M = models.IntegerField()
    AR_5_to_10M = models.IntegerField()
    AR_10_to_15M = models.IntegerField()
    AR_15_to_30M = models.IntegerField()
    AR_30_to_50M = models.IntegerField()
    AR_more_than_50M = models.IntegerField()
    pass_mark = models.IntegerField()

    def __str__(self):
        return "SME  Scores"


class Invitation(models.Model):
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=2000)
    source = models.CharField(max_length=200)

    def __str__(self):
        return "Invitation Preference"


class SMERegistration(models.Model):
    BUSINESS_CHOICE = (
        ('LL', 'Limited Liability'),
        ('RB', 'Registered Business Name'),
        ('P', 'Partnership'),
        ('U', 'Unregistered')
    )
    BUSINESS_YEARS_CHOICE = (
        ('L1', 'Less Than 1 Years'),
        ('1-3', '1-3 Years'),
        ('3-5', '3-5 Years'),
        ('O5', 'Over 5 Years'),
    )
    DATE_INCORPORATION_CHOICE = (
        ('L1', 'Less Than 1 Years'),
        ('1-3', '1-3 Years'),
        ('3-5', '3-5 Years'),
        ('O5', 'Over 5 Years'),
    )
    PERSONS_EMPLOYED_CHOICE = (
        ('L5', '0-5 Persons'),
        ('5-10', '5-10 Persons'),
        ('M10', 'More than 10 Persons'),
    )
    ANNUAL_REVENUE_CHOICE = (
        ('0-5', 'N0-N5M'),
        ('5-10', 'N5M-N10M'),
        ('10-15', 'N10M-N15M'),
        ('15-30', 'N15M-N30M'),
        ('M30', 'More than N30M')
    )
    PAYMENT_STATUS = (
        ('S', 'Success'),
        ('F', 'Failed'),
        ('U', 'Unknown')
    )

    CIRCUIT = (
        ('eko_cake_fair', "Eko Cake Fair"),
        ('skin_facial', 'Skin and Facial Beauty Fair')
    )

    circuit = models.CharField(
        max_length=20, choices=CIRCUIT)
    company_name = models.CharField(max_length=30)
    type_of_business = models.CharField(
        max_length=200, choices=BUSINESS_CHOICE)
    company_address = models.CharField(max_length=100)
    company_sector = models.CharField(max_length=20)
    years_business = models.CharField(
        max_length=20, choices=BUSINESS_YEARS_CHOICE)
    contact_person = models.CharField(max_length=20)
    company_person_designation = models.CharField(
        max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    description = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=250, blank=True, null=True)
    date_incorporation = models.CharField(
        max_length=200, choices=DATE_INCORPORATION_CHOICE, null=True, blank=True)
    contact_person2 = models.CharField(max_length=20, null=True, blank=True)
    employed_person = models.CharField(
        max_length=20, choices=PERSONS_EMPLOYED_CHOICE)
    annual_revenue = models.CharField(
        max_length=200, choices=ANNUAL_REVENUE_CHOICE)
    business_projection = models.TextField(
        max_length=500, null=True, blank=True)
    challenges = models.TextField(max_length=500, null=True, blank=True)
    outlets = models.CharField(max_length=500, null=True, blank=True)
    improve_business = models.TextField(max_length=500, null=True, blank=True)
    payment = models.CharField(
        null=True, blank=True, max_length=10, choices=PAYMENT_STATUS)
    payment_reference = models.CharField(max_length=15, null=True, blank=True)
    pdf = models.FileField(upload_to="documents", null=True, blank=True)
    invite = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="documents", blank=True, null=True)
    supporting_document = models.FileField(
        upload_to="documents", null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                             on_delete=models.CASCADE, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    def sme_scores(self):
        data = SMEScore.objects.get(pk=1)
        count = 0
        if self.type_of_business:
            if self.type_of_business == "LL":
                count += data.limited_liability
            elif self.type_of_business == "RB":
                count += data.registered_business_name
            elif self.type_of_business == "P":
                count += data.partnership
            elif self.type_of_business == "U":
                count += data.unregistered
        if self.email:
            # if self.email.split("@")[-1] in self.website.split("//")[-1]:
            count += data.email
        if self.website:
            count += data.website
        if self.date_incorporation:
            if self.date_incorporation == "L1":
                count += data.DOI_less_than_1_year
            elif self.date_incorporation == "1-3":
                count += data.DOI_1_to_3_year
            elif self.date_incorporation == "3-5":
                count += data.DOI_3_to_5_year
            elif self.date_incorporation == "O5":
                count += data.DOI_over_5_year
        if self.employed_person:
            if self.employed_person == "L5":
                count += data.NPE_0_to_5_persons
            elif self.employed_person == "5-10":
                count += data.NPE_5_to_10_persons
            elif self.employed_person == "M10":
                count += data.NPE_more_than_10_persons
        if self.annual_revenue:
            if self.annual_revenue == "0-5":
                count += data.AR_0_to_5M
            elif self.annual_revenue == "5-10":
                count += data.AR_5_to_10M
            elif self.annual_revenue == "10-15":
                count += data.AR_10_to_15M
            elif self.annual_revenue == "15-30":
                count += data.AR_15_to_30M
            elif self.annual_revenue == "M15":
                count += data.AR_30_to_50M
        return count

    def save(self, *args, **kwargs):
        data = {'company_name': self.company_name,
                "biz_sector": self.company_sector,
                "contact1": self.contact_person,
                "contact_designation": self.company_person_designation,
                "biz_years": next(j for i, j in self.BUSINESS_YEARS_CHOICE if i == self.years_business),
                # "doi": next(j for i, j in self.DATE_INCORPORATION_CHOICE if i == self.date_incorporation),
                "phone": self.phone_number,
                "annual_revenue": next(j for i, j in self.ANNUAL_REVENUE_CHOICE if i == self.annual_revenue),
                "company_address": self.company_address,
                "NOE": next(j for i, j in self.PERSONS_EMPLOYED_CHOICE if i == self.employed_person),
                "biz_improve": self.improve_business,
                "score": "Total Score: {}%".format(self.sme_scores()),
                'photo': self.photo}
        get_temp_file = utils.save_pdf(data)
        form_content = ContentFile(get_temp_file.getvalue())
        if self._state.adding:
            self.pdf.save("sme_reg_form_{}.pdf".format(
                self.pk), form_content, save=False)
        else:
            try:
                os.remove(self.pdf.path)
                self.pdf.save("sme_reg_form_{}.pdf".format(
                    self.pk), form_content, save=False)
            except:
                self.pdf.save("sme_reg_form_{}.pdf".format(
                    self.pk), form_content, save=False)
        super(SMERegistration, self).save(*args, **kwargs)
