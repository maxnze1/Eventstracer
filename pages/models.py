from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class HomeBanner(models.Model):
    video_banner = models.CharField(max_length=200, blank=False, null=True)


class WelcomeBlock(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    text = RichTextField()
    evt_video = models.CharField(max_length=200, blank=True, null=True)
    evt_video_image = models.ImageField(max_length=200, blank=True, null=True)
    linked_page = models.CharField(max_length=200, blank=True, null=True)
    button_text = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = ("Welcome Block")
        verbose_name_plural = ("Welcome Block")

    def __str__(self):
        return self.title


class CTASession(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True)
    background = models.ImageField(max_length=200, blank=False, null=True)
    button_title = models.CharField(max_length=200, blank=False, null=True)

    class Meta:
        verbose_name = ("Parallax Section")
        verbose_name_plural = ("Parallax Section")

    def __str__(self):
        return self.title


class CircuitNames(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200, blank=True, null=True)
    text = RichTextField()
    button = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


class FlowerConvention(CircuitNames):
    pass


class CakeFair(CircuitNames):
    pass


class BeadsPearls(CircuitNames):
    pass


class MusicConvention(CircuitNames):
    pass


class Gifts(CircuitNames):
    pass


class TopVideos(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    video = models.CharField(max_length=200)
    video_image = models.ImageField(max_length=200, blank=False, null=True)

    class Meta:
        verbose_name = ("Top Video")
        verbose_name_plural = ("Top Videos")


class PartnerLogos(models.Model):
    partner_name = models.CharField(max_length=200, blank=True, null=True)
    logo_image = models.ImageField(max_length=200, blank=False, null=True)

    def __str__(self):
        return self.partner_name

    class Meta:
        verbose_name = ("Partner Logo")
        verbose_name_plural = ("Partner Logos")


class ContactBlock(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class About(models.Model):
    page_title = models.CharField(max_length=200, blank=True, null=True)
    page_banner = models.ImageField(max_length=200, blank=True, null=True)
    image = models.ImageField(max_length=200, blank=True, null=True)
    content_title = models.CharField(max_length=200, blank=True, null=True)
    text = RichTextField()


class Advisory(models.Model):
    page_title = models.CharField(max_length=200, blank=True, null=True)
    page_banner = models.ImageField(blank=True, null=True)
    content_title = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    text = RichTextField(blank=True, null=True)


class Training(models.Model):
    page_title = models.CharField(max_length=200, blank=True, null=True)
    page_banner = models.ImageField(blank=True, null=True)
    content_title = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    text = RichTextField(blank=True, null=True)
