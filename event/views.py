from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    UpdateView
)
from .models import EventPage, Category
from ticketing.models import EventTicket
from taggit.models import Tag
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from users.models import CustomUser
from ticketing import utils
from django.contrib.auth.decorators import login_required
from uuid import uuid4
import googlemaps
# from .filters import EventFilter
from django.db.models import Q
gmaps = googlemaps.Client(key='AIzaSyCEtywbh0b6n4-jHcPWpdXYedd3JnockrY')


# class FilterView(ListView):
#     filterset_class = None

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         self.filterset = self.filterset_class(
#             self.request.GET, queryset=queryset)
#         return self.filterset.qs.distinct()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filterset'] = self.filterset
#         return context


class EventView(ListView):
    paginate_by = 12
    model = EventPage
    # filterset_class = EventFilter
    template_name = 'event/events.html'
    context_object_name = 'events'


# def event_list(request, tag_slug=None):
#     tag = None
#     # categories = Category.objects.all()
#     events = EventPage.published.all()
#     if tag_slug:
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         events = events.filter(tags__in=[tag])

#     context = {
#         'events': events,
#         'tag': tag,
#     }

#     return render(request, 'event/events.html', context)


def event_search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    events = EventPage.objects.filter(
        Q(title__icontains=search_text))

    return render(request, 'event/search_results.html', {'events': events})


def location_search(request):
    if request.method == 'POST':
        location_text = request.POST['location_text']
    else:
        location_text = ''
    location = EventPage.objects.filter(
        Q(location__icontains=location_text) | Q(address__icontains=location_text))

    return render(request, 'event/search_results.html', {'location': location})


def event_detail(request, slug):
    event = get_object_or_404(EventPage, slug=slug)

    event_tags_ids = event.tags.values_list('id', flat=True)
    similar_events = EventPage.published.filter(
        tags__in=event_tags_ids).exclude(id=event.id)
    similar_events = similar_events.annotate(
        same_tags=Count('tags')).order_by('-same_tags')[:4]
    if request.user.is_authenticated:
        interested = EventPage.objects.filter(interest=request.user)
        attending = EventPage.objects.filter(attending=request.user)
        ticket_check = EventTicket.objects.filter(
            title=event, user=CustomUser.objects.get(email=request.user.email))
    else:
        interested = attending = ticket_check = False
    stats = EventPage.objects.filter(
        slug=slug).aggregate(Count('interest'), Count('attending'))
    reference = str(uuid4().int >> 100)

    #address_cords = gmaps.geocode(event.address)[0]['geometry']['location']

    if request.method == "POST":
        get_status_payment = utils.verify_transaction(request.POST.get("reference"))
        if request.user:
            print(get_status_payment)
            if get_status_payment:
                ticket = EventTicket(title=event, start_date=event.start_date, end_date=event.end_date, amount=event.amount,
                                     payment_status='S')
                try:
                    next_id = EventTicket.objects.latest('id').pk + 1
                except:
                    next_id = 0 + 1
                ticket_id = "EVT-{0:06d}".format(next_id)
                ticket.ticket_id = ticket_id
                ticket.user = CustomUser.objects.get(email=request.user.email)
                ticket.save()
                utils.send_out_invitation(
                    "subject", [request.user.email], {'ticket_image': event.image, 'invitation': EventTicket.objects.get(title=event, user=CustomUser.objects.get(email=request.user.email)).ticket.path})
            return redirect(reverse('events:events-detail', kwargs={'slug': slug}))
        else:
            return redirect(reverse('accounts:login'))
    return render(request, 'event/event_detail.html', {'event': event, 'similar_events': similar_events, 'slug': slug,
                                                       'interested': interested, 'attending': attending, 'reference': reference,
                                                       'ticket_status': ticket_check, 'stats': stats})


class CreateEventView(LoginRequiredMixin, CreateView):
    model = EventPage
    fields = [
        'title',
        'category',
        'location',
        'address',
        'description',
        'start_date',
        'end_date',
        'amount',
        'organizer',
        'contact_person',
        'tags',
        'image',

    ]

    def get_form(self):
        form = super().get_form()
        form.fields['start_date'].widget = DateTimePickerInput()
        form.fields['end_date'].widget = DateTimePickerInput()
        form.fields['location'].initial = "Lagos"
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateViewEventView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EventPage
    fields = [
        'title',
        'category',
        'location',
        'address',
        'description',
        'start_date',
        'end_date',
        'amount',
        'organizer',
        'contact_person',
        'tags',
        'image',
    ]

    def get_form(self):
        location_cords = gmaps.geolocate(
            consider_ip=True, cell_towers=True, wifi_access_points=True)['location']
        location_state = gmaps.reverse_geocode(
            location_cords)[0]['address_components'][3]['long_name']
        form = super().get_form()
        form.fields['start_date'].widget = DateTimePickerInput()
        form.fields['end_date'].widget = DateTimePickerInput()
        form.fields['location'].initial = location_state
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False


class DeleteEventView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EventPage
    success_url = '/events'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.author:
            return True
        return False


# class PostByCategory(ListView):
#     model = EventPage
#     template_name = 'events/event_category.html'

#     def get_queryset(self):
#         self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
#         return EventPage.published.filter(category=self.category)

#     def get_context_data(self, **kwargs):
#         context = super(PostByCategory, self).get_context_data(**kwargs)
#         context['category'] = self.category
#         return context

@login_required
def interested(request, slug, status):
    user = CustomUser.objects.get(email=request.user.email)
    if status == 'False':
        event = EventPage.objects.get(slug=slug)
        event.interest.remove(user)
        event.save()
    else:
        event = EventPage.objects.get(slug=slug)
        event.interest.add(user)
        event.save()
    return redirect(reverse("events:events-detail", kwargs={'slug': slug}))


@login_required
def attending(request, slug, status):
    user = CustomUser.objects.get(email=request.user.email)
    if status == 'False':
        event = EventPage.objects.get(slug=slug)
        event.attending.remove(user)
        event.save()
    else:
        event = EventPage.objects.get(slug=slug)
        event.attending.add(user)
        event.save()
    return redirect(reverse("events:events-detail", kwargs={'slug': slug}))
