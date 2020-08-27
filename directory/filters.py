# import django_filters
# from .models import Directory, Category


# class DirectoryFilter(django_filters.FilterSet):

#     business_Type = django_filters.CharFilter(
#         lookup_expr='icontains', label='')
#     city = django_filters.CharFilter(lookup_expr='icontains', label='')
#     state = django_filters.CharFilter(lookup_expr='icontains',  label='')

#     class Meta:
#         model = Directory
#         fields = ['business_name', 'city', 'state']

#     def __init__(self, data, *args, **kwargs):
#         data = data.copy()
#         data.setdefault('format', 'paperback')
#         data.setdefault('order', '-added')
#         super().__init__(data, *args, **kwargs)
