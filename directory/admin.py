from django.contrib import admin

from .models import(
    Category,
    Directory,


)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('business_name',)
    prepopulated_fields = {'slug': ('business_name',)}


admin.site.register(Directory, DirectoryAdmin)
