from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Directory, Category
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from .filters import DirectoryFilter


class FilterView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class DirectoryView(FilterView):
    paginate_by = 5
    model = Directory
    # filterset_class = DirectoryFilter
    template_name = 'directory/directory.html'

    context_object_name = 'directories'

    # def get(self, request):
    #     cat_id = self.kwargs.get("slug")
    #     if cat_id:
    #         category = get_object_or_404(Category, pk=cat_id)
    #         directories = directories.filter(category=category)
    #     return render(request, 'directory/directory.html')

    # def get_queryset(self,  *args, **kwargs):
    #     self.category = Category.objects.all()
    #     self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
    #     return Directory.objects.filter(category=self.category)

    # def get_context_data(self, **kwargs):
    #     context = super(DirectoryView, self).get_context_data(**kwargs)
    #     context['category'] = self.category
    #     return context


class DirectoryCategoryView(ListView):
    paginate_by = 5
    model = Directory
    template_name = 'directory/category.html'

    def get_queryset(self):
        return Directory.objects.filter(category_id=self.kwargs.get('pk'))

    # model = Directory
    # paginate_by = 5
    # template_name = 'directory/directory.html'
    # context_object_name = 'directories'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = DirectoryFilter(
    #         self.request.GET, queryset=Directory.objects.all())
    #     return context


# def directory_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     directories = Directory.objects.all()
#     page = request.GET.get('page', 1)
#     paginator = Paginator(directories, 5)
#     try:
#         directories = paginator.page(page)
#     except PageNotAnInteger:
#         directories = paginator.page(1)
#     except EmptyPage:
#         directories = paginator.page(paginator.num_pages)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         directories = directories.filter(category=category)

#     return render(request, 'directory/directory.html', {'categories': categories, 'category': category, 'directories': directories})


def directory_detail(request, id, slug):
    directory = get_object_or_404(Directory, slug=slug)
    return render(request, 'directory/directory_detail.html', {'directory': directory})


class CreateDirectoryView(CreateView):
    model = Directory
    fields = [
        'category',
        'business_name',
        'business_address',
        'state',
        'city',
        'phone_number',
        'email',
        'track_record',
        'company_logo',
        'product_image',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateViewDirectory(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Directory
    fields = [
        'category',
        'business_name',
        'business_address',
        'state',
        'city',
        'phone_number',
        'email',
        'track_record',
        'company_logo',
        'product_image',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        directory = self.get_object()
        if self.request.user == directory.author:
            return True
        return False


# class DirectoryDetailView(DetailView):
#     model: Directory
#     template_name = 'directory/directory_detail.html'
#     context_object_name = 'directory'
