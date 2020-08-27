from django import forms
from croppie.fields import CroppieField


class SMERegistration1(forms.Form):
    BUSINESS_CHOICE = (
        ('', "Select an Option"),
        ('LL', 'Limited Liability'),
        ('RB', 'Registered Business Name'),
        ('P', 'Partnership'),
        ('U', 'Unregistered')
    )
    BUSINESS_YEARS_CHOICE = (
        ('', "Select an Option"),
        ('L1', 'Less Than 1 Years'),
        ('1-3', '1-3 Years'),
        ('3-5', '3-5 Years'),
        ('O5', 'Over 5 Years'),
    )

    CIRCUIT = (
        ('eko_cake_fair', "Eko Cake Fair"),
        ('skin_facial', 'Skin and Facial Beauty Fair')
    )

    circuit = forms.ChoiceField(
        label="Select Circuit", choices=CIRCUIT, widget=forms.Select)
    company_name = forms.CharField(max_length=30)
    type_of_business = forms.ChoiceField(
        choices=BUSINESS_CHOICE, widget=forms.Select)
    supporting_document = forms.FileField(widget=forms.FileInput(
        attrs={'style': 'display:none', 'class': 'form-control'}), required=False)
    company_address = forms.CharField(max_length=100)
    company_sector = forms.CharField(
        max_length=20, label="Industry", required=False)
    years_business = forms.ChoiceField(label="Number of years in business", choices=BUSINESS_YEARS_CHOICE,
                                       widget=forms.Select)
    contact_person = forms.CharField(max_length=20, required=False)
    company_person_designation = forms.CharField(max_length=20, required=False)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)


class SMERegistration2(forms.Form):
    DATE_INCORPORATION_CHOICE = (
        ('', "Select an Option"),
        ('L1', 'Less Than 1 Years'),
        ('1-3', '1-3 Years'),
        ('3-5', '3-5 Years'),
        ('O5', 'Over 5 Years'),
    )
    PERSONS_EMPLOYED_CHOICE = (
        ('', "Select an Option"),
        ('L5', '0-5 Persons'),
        ('5-10', '5-10 Persons'),
        ('M10', 'More than 10 Persons'),
    )
    ANNUAL_REVENUE_CHOICE = (
        ('', "Select an Option"),
        ('0-5', 'N0-N5M'),
        ('5-10', 'N5M-N10M'),
        ('10-15', 'N10M-N15M'),
        ('15-30', 'N15M-N30M'),
        ('M30', 'More than N30M')
    )
    description = forms.CharField(
        widget=forms.Textarea, label="What does your business do?", required=False)
    website = forms.CharField(
        max_length=250, label="Website address", required=False)
    date_incorporation = forms.ChoiceField(choices=DATE_INCORPORATION_CHOICE, widget=forms.Select,
                                           label="Date of incorporation", required=False)
    contact_person = forms.CharField(max_length=20)
    employed_person = forms.ChoiceField(choices=PERSONS_EMPLOYED_CHOICE, widget=forms.Select,
                                        label="Number of persons employed")
    annual_revenue = forms.ChoiceField(
        choices=ANNUAL_REVENUE_CHOICE, widget=forms.Select)


class SMERegistration3(forms.Form):
    business_projection = forms.CharField(
        max_length=500, widget=forms.Textarea, label="Where do you see your business in the next 3 years", required=False)
    challenges = forms.CharField(
        max_length=500, label="Describe three key challenges that your business is facing today", widget=forms.Textarea, required=False)
    outlets = forms.CharField(
        max_length=500, label="How many outlet does your business have?")
    improve_business = forms.CharField(
        max_length=500, label="What is the single most important thing that will improve your business?", widget=forms.Textarea, required=False)
    photo = forms.ImageField(
        help_text="You are adviced to use an image size of 235X230", required=False)


class SMERegistration4(forms.Form):
    confirm = forms.BooleanField(required=False)


class SMERegistrationPayment(forms.Form):
    PAYMENT_TYPE_CHOICE = (
        ("select", "---Select---"),
        ("100000", "Lagos Flower Convention"),
        ("100000", "Cake Delight"),
        ("100000", "Leather Fashion Fair"),
        ("100000", "Gifts & Wraps"),
        ("100000", "Skin & Facial Beauty Fair"),
        ("100000", "Oil & Fragrance Bazaar"),
        ("100000", "Pearls & Beads Exhibition"),
        ("100000", "Valentine Flower Festival"),
    )
    payment_type = forms.ChoiceField(
        choices=PAYMENT_TYPE_CHOICE, widget=forms.Select)
    reference = forms.CharField(max_length=15, widget=forms.HiddenInput)
