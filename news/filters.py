import django_filters
from .models import Directory, Category


class NewsFilter(django_filters.FilterSet):

    business_name = django_filters.CharFilter(
        lookup_expr='icontains', label='Business name')
    city = django_filters.CharFilter(lookup_expr='icontains', label='City')
    state = django_filters.CharFilter(lookup_expr='icontains',  label='State')

    class Meta:
        model = Directory
        fields = ['business_name', 'city', 'state']

    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        data.setdefault('format', 'paperback')
        data.setdefault('order', '-added')
        super().__init__(data, *args, **kwargs)
