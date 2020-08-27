from django.shortcuts import get_object_or_404
from ..models import SmeCircuit, Category
from django import template

register = template.Library()


@register.inclusion_tag('sme/components/sme_cat_menu.html')
def sme_category(category_slug=None):
    category = None
    categories = Category.objects.all()
    sme = SmeCircuit.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        sme = sme.filter(category=category)
    return {'categories': categories, 'category': category}
