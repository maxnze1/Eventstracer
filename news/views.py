from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import News, Category
from taggit.models import Tag
from django.db.models import Count
from django.db.models import Q


# class NewsView(ListView):
#     paginate_by = 5
#     model = News
#     template_name = 'news/news.html'
#     context_object_name = 'news'

def news_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    news = News.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(news, 5)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        news = news.filter(category=category)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    context = {
        'news': news,
        'categories': categories,
        'category': category
    }

    return render(request, 'news/news.html', context)


def news_search(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    news = News.objects.filter(
        Q(title__icontains=search_text) | Q(body__icontains=search_text))
    return render(request, 'news/search_results.html', {'news': news})


def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)

    news_tags_ids = news_item.tags.values_list('id', flat=True)
    similar_news = News.published.filter(
        tags__in=news_tags_ids).exclude(id=news_item.id)
    similar_news = similar_news.annotate(
        same_tags=Count('tags')).order_by('-same_tags')[:4]

    return render(request, 'news/news_detail.html', {'news_item': news_item, 'similar_news': similar_news})


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
