from django.contrib import admin
from .models import GalleryBanner, Gallery, GalleryImage, GalleryVideo

# Inline admin classes to handle related models
class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1  # Number of empty forms to display by default

class GalleryVideoInline(admin.TabularInline):
    model = GalleryVideo
    extra = 1  # Number of empty forms to display by default

# Gallery admin configuration
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_title', 'year', 'slug')
    search_fields = ('title', 'main_title', 'slug')
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug based on title
    inlines = [GalleryImageInline, GalleryVideoInline]  # Include related images and videos

# GalleryBanner admin configuration
class GalleryBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)

# GalleryImage admin configuration
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'image')
    search_fields = ('gallery__title',)  # Searching images by related gallery title

# GalleryVideo admin configuration
class GalleryVideoAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'video_url', 'thumbnail')
    search_fields = ('gallery__title', 'video_url')

# Registering models with the admin site
admin.site.register(GalleryBanner, GalleryBannerAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(GalleryVideo, GalleryVideoAdmin)
