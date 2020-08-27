from django.shortcuts import get_object_or_404
from ..models import Directory, Category
from django import template

register = template.Library()


@register.inclusion_tag('directory/directory_components/directory_cat_menu.html')
def directory_category(category_slug=None):
    category = None
    categories = Category.objects.all()
    directory = Directory.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        directory = directory.filter(category=category)
    return {'categories': categories, 'category': category, 'directory': directory}


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()


@register.inclusion_tag('directory/directory_components/cat_menu.html')
def d_category(category_slug=None):
    category = None
    categories = Category.objects.all()
    directory = Directory.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        directory = directory.filter(category=category)
    return {'categories': categories, 'category': category}
