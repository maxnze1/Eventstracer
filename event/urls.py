from django.urls import path, include

from .views import event_detail, event_search, location_search, EventView, CreateEventView, UpdateViewEventView, DeleteEventView, interested, attending
app_name = 'events'

urlpatterns = [
    path('search/', event_search),
    path('location/', location_search),
    path('', EventView.as_view(), name='events'),
    path('eventlisting/<tag_slug>/', EventView.as_view(), name='events_by_tags'),
    path('events/<slug>/', event_detail, name='events-detail'),
    path('events/<slug>/update/',
         UpdateViewEventView.as_view(), name='events-update'),
    path('events/<slug>/delete/',
         DeleteEventView.as_view(), name='events-delete'),
    path('events/', CreateEventView.as_view(), name='create'),
    path('interest/<slug>/<status>', interested, name='interested'),
    path('attending/<slug>/<status>', attending, name='attending'),

]
