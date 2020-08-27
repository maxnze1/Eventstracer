from django.db import models
from django.conf import settings
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='publish')


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    slug = AutoSlugField(populate_from='name', editable=True)
    cat_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('news:news_cat', args=[self.slug])


class News(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish')
    )

    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', editable=True, max_length=200)
    body = RichTextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='news_author', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='events_pics')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS, default='publish')

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:news-detail', args=[self.slug])
