from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager


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
        return reverse('directory:directory_list_by_cat',  kwargs={'pk': self.pk})


class Directory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    business_name = models.CharField("", max_length=200, blank=False)
    slug = models.SlugField(max_length=250)
    track_record = models.TextField()
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone_number = PhoneNumberField()
    business_address = models.TextField()
    state = models.CharField("", max_length=120, blank=True, null=True)
    city = models.CharField("", max_length=120, blank=True, null=True)
    company_logo = models.ImageField(
        default='directory/default_logo.jpg', upload_to='directory', blank=True, null=True)
    product_image = models.ImageField(
        default='directory/default_img.jpg', upload_to='directory', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.business_name

    def _get_unique_slug(self):
        slug = slugify(self.business_name)
        unique_slug = slug
        num = 1
        while Directory.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('directory:directory-detail', args=[self.id, self.slug])

    def get_update_link(self):
        return reverse('directory:update', args=[self.id, self.slug])
