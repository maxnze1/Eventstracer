from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)
    slug = models.SlugField(max_length=200)
    cat_image = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Videos(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=200, blank=False, null=True)
    slug = models.SlugField(max_length=200)
    video_url = models.CharField(max_length=200, blank=False, null=True)
    video_image = models.ImageField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.video_title


class SixtySeconds(Videos):
    class Meta:
        verbose_name = 'sixtyseconds'


class EventSpectrum(Videos):
    class Meta:
        verbose_name = 'EventSpectrum'


class BizVia(Videos):
    class Meta:
        verbose_name = 'BizVia'


class BusinessSense(Videos):
    class Meta:
        verbose_name = 'BusinessSense'


class Exclusive(Videos):
    class Meta:
        verbose_name = 'Exclusive'


class Insight(Videos):
    class Meta:

        verbose_name = 'Insight'


class StartUpNaija(Videos):
    class Meta:

        verbose_name = 'StartUpNaija'


class HighlightVideo(models.Model):
    video_title = models.CharField(max_length=200, blank=True, null=True)
    video_url = models.CharField(max_length=200, blank=False, null=True)

    class Meta:
        verbose_name = 'HighlightVideo'

    def __str__(self):
        return self.video_title


class EventTV(models.Model):
    video_title = models.CharField(max_length=200, blank=True, null=True)
    video_url = models.CharField(max_length=200, blank=False, null=True)

    class Meta:
        verbose_name = 'Event TV'

    def __str__(self):
        return self.video_title
