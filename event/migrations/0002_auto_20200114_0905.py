# Generated by Django 2.0.13 on 2020-01-14 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='attending',
            field=models.ManyToManyField(blank=True, related_name='attending_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='interest',
            field=models.ManyToManyField(blank=True, related_name='interested_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]