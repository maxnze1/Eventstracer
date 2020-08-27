from django.contrib import admin


from .models import(
    EventSpectrum,
    BizVia,
    BusinessSense,
    StartUpNaija,
    Exclusive,
    Insight,
    Category,
    HighlightVideo,
    EventTV,
    SixtySeconds,
)


class SixtySecondsAdmin(admin.ModelAdmin):
    list_display = ['video_title']


admin.site.register(SixtySeconds, SixtySecondsAdmin)


class EventTVAdmin(admin.ModelAdmin):
    list_display = ['video_title']


admin.site.register(EventTV, EventTVAdmin)


class EventSpectrumAdmin(admin.ModelAdmin):
    list_display = ['video_title', 'category']
    prepopulated_fields = {'slug': ('video_title',)}


admin.site.register(EventSpectrum, EventSpectrumAdmin)


class BizViaAdmin(admin.ModelAdmin):
    list_display = ['video_title', 'category']
    prepopulated_fields = {'slug': ('video_title',)}


admin.site.register(BizVia, BizViaAdmin)


class BusinessSenseAdmin(admin.ModelAdmin):
    list_display = ['video_title', 'category']
    prepopulated_fields = {'slug': ('video_title',)}


admin.site.register(BusinessSense, BusinessSenseAdmin)


class ExclusiveAdmin(admin.ModelAdmin):
    list_display = ['video_title', 'category']
    prepopulated_fields = {'slug': ('video_title',)}


admin.site.register(Exclusive, ExclusiveAdmin)


class InsightAdmin(admin.ModelAdmin):
    list_display = ['video_title', 'category']
    prepopulated_fields = {'slug': ('video_title',)}


admin.site.register(Insight, InsightAdmin)


class StartUpNaijaAdmin(admin.ModelAdmin):
    list_display = ['video_title', 'category']
    prepopulated_fields = {'slug': ('video_title',)}


admin.site.register(StartUpNaija, StartUpNaijaAdmin)


class HighlightVideoAdmin(admin.ModelAdmin):
    list_display = ['video_title']


admin.site.register(HighlightVideo, HighlightVideoAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
