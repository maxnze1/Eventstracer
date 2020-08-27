from django.contrib import admin


from .models import SmeCircuit, Category, SmeLandingPage, SmeThumbnail, SmeBanner


class SmeCircuitAdmin(admin.ModelAdmin):
    list_display = ['content_title', 'category']
    prepopulated_fields = {'slug': ('content_title',)}


admin.site.register(SmeCircuit, SmeCircuitAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)



class SmeLandingPageAdmin(admin.ModelAdmin):
    list_display = ['content_title']
    prepopulated_fields = {'slug': ('content_title',)}


admin.site.register(SmeLandingPage, SmeLandingPageAdmin)


class SmeThumbnailAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(SmeThumbnail, SmeThumbnailAdmin)


class SmeBannerAdmin(admin.ModelAdmin):
    pass


admin.site.register(SmeBanner, SmeBannerAdmin)

