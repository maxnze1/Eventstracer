from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)
    cat_image = models.ImageField(blank=True, null=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sme:sme_list_by_cat', args=[self.slug])


class SmeCircuit(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content_title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=250)
    page_banner = models.ImageField(blank=True)
    content_image = models.ImageField()
    body = RichTextField()

    class Meta:
        verbose_name = 'SME Circuit'
        verbose_name_plural = 'SME Circuit'

    def __str__(self):
        return self.content_title



class SmeLandingPage(models.Model):
    content_title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=250)
    content_image = models.ImageField(blank=True, null=True)
    body = RichTextField()

    class Meta:
        verbose_name = 'SME Landing Page'
        verbose_name_plural = 'SME Landing Page'

    def __str__(self):
        return self.content_title

class SmeBanner(models.Model):
    banner_image = models.ImageField(blank=True, null=True)
    banner_title = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.banner_title

class SmeThumbnail(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    linked_page = models.CharField(max_length=120)

    def __str__(self):
        return self.title

