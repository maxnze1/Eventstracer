from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileUpdateForm
from registrations.models import SMERegistration
from event.models import EventPage
from ticketing.models import EventTicket
import csv


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('users:profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'smes': SMERegistration.objects.filter(user=request.user),
        'events': EventPage.objects.filter(author=request.user),
        'tickets': EventTicket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context)


@login_required
def interested_csv(request, slug):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=interested.csv'
    writer = csv.writer(response)
    # You can add additional fields here
    writer.writerow(['S/N', 'interested email'])
    for ind, item in enumerate(EventPage.objects.get(author=request.user, slug=slug).interest.all()):
        writer.writerow([ind+1, item.email])
    return response


@login_required
def attending_csv(request, slug):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=attending.csv'
    writer = csv.writer(response)
    writer.writerow(['S/N', 'attending email'])
    # You can add additional fields here
    for ind, item in enumerate(EventPage.objects.get(author=request.user, slug=slug).interest.all()):
        writer.writerow([ind+1, item.email])
    return response


@login_required
def ticketing_csv(request, slug):
    event = EventPage.objects.get(slug=slug)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename={}_ticket_list.csv'.format(
        slug)
    writer = csv.writer(response)
    writer.writerow(['S/N', 'Ticket ID', 'email', 'amount'])
    for ind, item in enumerate(EventTicket.objects.filter(title=event)):
        writer.writerow(
            [ind + 1, item.ticket_id, item.user.email, item.amount])
    return response
