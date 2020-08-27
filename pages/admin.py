from django.contrib import admin

from .models import(
    HomeBanner,
    PartnerLogos,
    CTASession,
    WelcomeBlock,
    TopVideos,
    FlowerConvention,
    CakeFair,
    BeadsPearls,
    MusicConvention,
    ContactBlock,
    Gifts,
    About,
    Advisory,
    Training,
)


class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ['video_banner']


admin.site.register(HomeBanner, HomeBannerAdmin)


class CTASessionAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(CTASession, CTASessionAdmin)


class WelcomeBlockAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(WelcomeBlock, WelcomeBlockAdmin)


class TopVideosAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(TopVideos, TopVideosAdmin)


class PartnerLogosAdmin(admin.ModelAdmin):
    list_display = ['partner_name']


admin.site.register(PartnerLogos, PartnerLogosAdmin)


class FlowerConventionAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(FlowerConvention, FlowerConventionAdmin)


class CakeFairAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(CakeFair, CakeFairAdmin)


class BeadsPearlsAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(BeadsPearls, BeadsPearlsAdmin)


class MusicConventionAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(MusicConvention, MusicConventionAdmin)


class ContactBlockAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(ContactBlock, ContactBlockAdmin)


class GiftsAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Gifts, GiftsAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['page_title']


admin.site.register(About, AboutAdmin)


class AdvisoryAdmin(admin.ModelAdmin):
    list_display = ['page_title']


admin.site.register(Advisory, AdvisoryAdmin)


class TrainingAdmin(admin.ModelAdmin):
    list_display = ['page_title']


admin.site.register(Training, TrainingAdmin)
