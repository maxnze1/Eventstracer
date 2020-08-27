from django.urls import path, include

from .views import news_detail, news_list, news_search
app_name = 'news'

urlpatterns = [
    path('search/', news_search),
    path('', news_list, name='news-list'),
    path('news/<tag_slug>/', news_list, name='news_by_tags'),
    path('news/<slug>', news_detail, name='news-detail'),
    path('<category_slug>/', news_list, name='news_cat'),

]
