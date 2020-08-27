from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import(
    EventSpectrum,
    Exclusive,
    BizVia,
    BusinessSense,
    Insight,
    StartUpNaija,
    HighlightVideo,
    EventTV,
    SixtySeconds,
)


class VideoView(ListView):
    context_object_name = 'eventspectrum'
    template_name = 'videos/videos.html'
    queryset = EventSpectrum.objects.all()

    def get_context_data(self, **kwargs):
        context = super(VideoView, self).get_context_data(**kwargs)
        context['exclusive'] = Exclusive.objects.all()
        context['bizvia'] = BizVia.objects.all()
        context['business_sense'] = BusinessSense.objects.all()
        context['insight'] = Insight.objects.all()
        context['startupnaija'] = StartUpNaija.objects.all()
        context['sixtysec'] = SixtySeconds.objects.all()
        context['highlightvideo'] = HighlightVideo.objects.all()
        return context


class EventTVView(ListView):
    context_object_name = 'event_tv'
    template_name = 'videos/events_tv.html'
    queryset = EventTV.objects.all()
