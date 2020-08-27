from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.conf import settings
from django.core.files.base import ContentFile
from ticketing import utils
import os


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
        return reverse('events:events_by_category', args=[self.slug])


STATUS = (
    ('draft', 'Draft'),
    ('publish', 'Publish')
)


class EventPage(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', editable=True, max_length=200)
    location = models.CharField(max_length=200)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='events_pics')
    address = models.CharField(max_length=200)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    organizer = models.CharField(max_length=100, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    has_ticket = models.BooleanField(default=False)
    amount = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS, default='publish')
    featured = models.BooleanField(default=False)
    featured_image = models.ImageField(
        upload_to='events_pics', blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    interest = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="interested_users")
    attending = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="attending_users")

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-featured',)
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events:events-detail', args=[self.slug])
