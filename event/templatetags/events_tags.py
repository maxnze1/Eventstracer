from ..models import EventPage
from django.shortcuts import render, get_object_or_404, redirect, reverse
from taggit.models import Tag
from django import template
from datetime import datetime

register = template.Library()


@register.inclusion_tag('events/top_events.html')
def top_events(count=20,  tag_slug=None):
    tag = None
    top_events = EventPage.published.order_by('-created')[:count]
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        events = events.filter(tags__in=[tag])

    return {'top_events': top_events, 'tag': tag}


@register.filter
def expire_status(id):
    return False if EventPage.objects.filter(id=id, start_date__lt=datetime.now()) else True


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()
