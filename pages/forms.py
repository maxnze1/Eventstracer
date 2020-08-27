from django import forms

CATEGORIES = (
    ('', 'Choose...',),
    ('Event Owner', 'Event Owner',),
    ('Event Venue Owner, owner', 'Event Venue Owner',),
    ('Event Sponsor', 'Event Sponsor',),
    ('Event Exhibitor', 'Event Exhibitor',),
    ('Others', 'Others',),
)

SERVICES = (
    ('', 'Choose...',),
    ('Event Creation', 'Event Creation',),
    ('Event Design', 'Event Design',),
    ('Event Design', 'Event Naming',),
    ('venue_selection', 'Venue Selection',),
    ('Business Marketing', 'Business Marketing',),
    ('events_sponsorship', 'Event Sponsorship',),
    ('Event Sponsorship', 'Partnership Opportunities',),
    ('Digital Strategy', 'Digital Strategy',),
    ('Other Services', 'Other Services',),
)


TRAINING = (
    ('', 'Choose...',),
    ('Finance', 'Finance',),
    ('Marketing', 'Marketing',),
    ('Presenting', 'Presenting',),
    ('Editing', 'Editing',),
    ('Writing', 'Writing',),
    ('Web Design', 'Web Design',),
    ('Digital Marketing', 'Digital Marketing',),
    ('Business Journalism', 'Business Journalism',),
)

class AdvisoryForm(forms.Form):
    surname = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone_number = forms.IntegerField(required=True)
    company_name = forms.CharField(max_length=200)
    company_address = forms.CharField(max_length=200)
    company_email = forms.CharField()
    category = forms.ChoiceField(choices=CATEGORIES)
    services = forms.ChoiceField(choices=SERVICES)




class TrainingForm(forms.Form):
    surname = forms.CharField(max_length=200)
    firstname = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone_number = forms.IntegerField(required=True)
    company_name = forms.CharField(max_length=200)
    company_address = forms.CharField(max_length=200)
    company_email = forms.CharField()
    training = forms.ChoiceField(choices=TRAINING)

