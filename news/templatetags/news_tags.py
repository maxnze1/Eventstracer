from django.shortcuts import get_object_or_404
from ..models import News, Category
from django import template

register = template.Library()


@register.inclusion_tag('news/top_events.html')
def top_events(count=5):
    top_events = News.published.order_by('-status')[:5]
    return {'top_events': top_events}


@register.inclusion_tag('news/news_cat.html')
def news_category(category_slug=None):
    category = None
    categories = Category.objects.all()
    news = News.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        news = news.filter(category=category)
    return {'categories': categories, 'category': category}


@register.inclusion_tag('news/top_news.html')
def top_news(count=2):
    top_news = News.published.order_by('-created')[:2]
    return {'top_news': top_news}
