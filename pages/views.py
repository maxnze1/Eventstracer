from django.shortcuts import render
from django.views.generic import ListView
from .forms import AdvisoryForm, TrainingForm
from django.core.mail import send_mail


from .models import(
    HomeBanner,
    PartnerLogos,
    CTASession,
    WelcomeBlock,
    TopVideos,
    FlowerConvention,
    CakeFair,
    BeadsPearls,
    MusicConvention,
    ContactBlock,
    Gifts,
    About,
    Advisory,
    Training
)


class HomeView(ListView):
    context_object_name = 'data'
    template_name = 'pages/home.html'
    queryset = HomeBanner.objects.all()

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['cta'] = CTASession.objects.all()
        context['welcome'] = WelcomeBlock.objects.all()
        context['flower'] = FlowerConvention.objects.all()
        context['topvideos'] = TopVideos.objects.all()
        context['beads'] = BeadsPearls.objects.all()
        context['music'] = MusicConvention.objects.all()
        context['cake'] = CakeFair.objects.all()
        context['contact'] = ContactBlock.objects.all()
        context['logos'] = PartnerLogos.objects.all()
        context['gifts'] = Gifts.objects.all()
        return context


class AboutView(ListView):
    context_object_name = 'about_data'
    template_name = 'pages/about.html'
    queryset = About.objects.all()


class AdvisoryView(ListView):
    context_object_name = 'advisory_data'
    template_name = 'pages/advisory_page.html'
    queryset = Advisory.objects.all()


class TrainingView(ListView):
    context_object_name = 'training_data'
    template_name = 'pages/training_page.html'
    queryset = Training.objects.all()


def advisory_request_form(request):
    sent = False
    queryset = Advisory.objects.all()
    if request.method == 'POST':
        advisory_form = AdvisoryForm(request.POST or None)
        if advisory_form.is_valid():
            clean_advisory_data = advisory_form.cleaned_data
            subject = f"Advisory services request from {clean_advisory_data['firstname']}"
            message = f"Name: {clean_advisory_data['surname']} {clean_advisory_data['firstname']}\n Email: {clean_advisory_data['email']}\n Phone number: {clean_advisory_data['phone_number']}\n Company name: {clean_advisory_data['company_name']}\n Company address: {clean_advisory_data['company_address']}\n Company email: {clean_advisory_data['company_email']}\n Company email: {clean_advisory_data['company_email']}\n Advisory Category: {clean_advisory_data['category']}\n Advisory Services: {clean_advisory_data['services']}\n"
            send_mail(subject,
                      message,
                      'info@smallbizeventciruit.com',
                      ['info@smallbizeventciruit.com'],
                      fail_silently=False
                      )
            sent = True

    else:
        advisory_form = AdvisoryForm()

    return render(request, 'pages/advisory_page.html', {'advisory_form': advisory_form, 'queryset': queryset, 'sent': sent})





def training_request_form(request):
    sent = False
    queryset = Training.objects.all()
    if request.method == 'POST':
        training_form = TrainingForm(request.POST or None)
        if training_form.is_valid():
            clean_training_data = training_form.cleaned_data
            subject = f"Training request from {clean_training_data['firstname']}"
            message = f"Name: {clean_training_data['surname']} {clean_training_data['firstname']}\n Email: {clean_training_data['email']}\n Phone number: {clean_training_data['phone_number']}\n Company name: {clean_training_data['company_name']}\n Company address: {clean_training_data['company_address']}\n Company email: {clean_training_data['company_email']}\n Company email: {clean_training_data['company_email']}\n Training Required: {clean_training_data['training']}\n "
            send_mail(subject,
                      message,
                      'info@smallbizeventciruit.com',
                      ['info@smallbizeventciruit.com'],
                      fail_silently=False
                      )
            sent = True

    else:
        training_form = TrainingForm()

    return render(request, 'pages/training_page.html', {'training_form': training_form, 'queryset': queryset, 'sent': sent})

