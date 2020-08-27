from django import template
from event.models import EventPage
from ticketing.models import EventTicket

register = template.Library()


@register.filter
def ticket_bought(slug):
    event = EventPage.objects.get(slug=slug)
    num = EventTicket.objects.filter(title=event).count()
    return num
