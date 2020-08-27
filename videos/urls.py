from django.urls import path, include

from .views import VideoView, EventTVView
app_name = 'videos'

urlpatterns = [
    path('videos/', VideoView.as_view(), name='videos'),
    path('tv/', EventTVView.as_view(), name='tv'),

]
