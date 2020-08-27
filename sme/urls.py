from django.urls import path

from .views import sme_pages, sme_landing_page

app_name = 'sme'

urlpatterns = [
    path('', sme_pages, name='sme'),
    path('home/', sme_landing_page, name='sme-home'),
    path('<category_slug>/', sme_pages, name='sme_list_by_cat'),

]
