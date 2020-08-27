from django.shortcuts import render, get_object_or_404

from .models import SmeCircuit, Category, SmeLandingPage, SmeThumbnail, SmeBanner


def sme_pages(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    sme = SmeCircuit.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        sme = sme.filter(category=category)

    return render(request, 'sme/sme.html', {'categories': categories, 'category': category, 'sme': sme})



def sme_landing_page(request):
    sme_banner = SmeBanner.objects.all()
    thumbnail = SmeThumbnail.objects.all()
    page_data = SmeLandingPage.objects.all()
    return render(request, 'sme/sme_landing_page.html', {'page_data': page_data, 'thumbnail': thumbnail, 'sme_banner': sme_banner})

