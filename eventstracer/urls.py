from api.router import router
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import forms_builder.forms.urls
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('pages/', include('django.contrib.flatpages.urls')),
    path('admin/', include('smuggler.urls')),
    path('admin/', admin.site.urls),
    path('forms/', include(forms_builder.forms.urls)),
    path('', include('pages.urls')),
    path('sme/', include('sme.urls')),
    path('events/', include('event.urls', namespace='events')),
    path('news/', include('news.urls')),
    path('directory/', include('directory.urls', namespace='directory')),
    path('', include('videos.urls')),
    path('', include('users.urls')),
    path('registrations/', include('registrations.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
