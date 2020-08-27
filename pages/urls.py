from django.urls import path

from .views import HomeView, AboutView, AdvisoryView, TrainingView, advisory_request_form, training_request_form

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about-us'),
     path('advisory/', advisory_request_form, name='advisory-form'),
    path('training/', training_request_form, name='training'),
    
]
