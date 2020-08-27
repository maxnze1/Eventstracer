from django.urls import path

from .views import profile, interested_csv, attending_csv, ticketing_csv

app_name = 'users'

urlpatterns = [
    path('users/profile/', profile, name='profile'),
    path('users/interested/<slug>/', interested_csv, name='interested'),
    path('users/attending/<slug>', attending_csv, name='attending'),
    path('users/ticketing/<slug>', ticketing_csv, name='ticketing'),
]

