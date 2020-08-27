from django.contrib import admin
from .models import EventPage, Category


class EventPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'organizer', 'contact_person',
                    'has_ticket', 'status', 'created', 'start_date', 'end_date',)
    filter_horizontal = ('interest', 'attending',)

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(EventPage, EventPageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
