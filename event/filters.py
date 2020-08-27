# import django_filters
# from .models import EventPage


# class EventFilter(django_filters.FilterSet):

#     title = django_filters.CharFilter(
#         lookup_expr='icontains', label='Event Title')
#     location = django_filters.CharFilter(
#         lookup_expr='icontains', label='Location')
#     address = django_filters.CharFilter(
#         lookup_expr='icontains',  label='Address')

#     class Meta:
#         model = EventPage
#         fields = ['title', 'location', 'address']

#     def __init__(self, data, *args, **kwargs):
#         data = data.copy()
#         data.setdefault('format', 'paperback')
#         data.setdefault('order', '-added')
#         super().__init__(data, *args, **kwargs)
