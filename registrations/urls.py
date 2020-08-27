from django.urls import path
from registrations import views
from django.views.generic import TemplateView

app_name = "registrations"

urlpatterns = [
    path('sme-form', views.SMERegistrationWizard.as_view(), name='sme'),
    path('thank-you', TemplateView.as_view(template_name="sme4-form.html"),
         name='thank-you'),
    # path('test/', views.test)
]
