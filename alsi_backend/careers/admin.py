from django.contrib import admin
from .models import CareersBanner, CareersForm

class CareersBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)

class CareersFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('submitted_at',)
    readonly_fields = ('submitted_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'message', 'referer_url', 'submitted_url', 'file')
        }),
        ('Submission Details', {
            'fields': ('submitted_at',),
            'classes': ('collapse',)
        }),
    )

admin.site.register(CareersBanner, CareersBannerAdmin)
admin.site.register(CareersForm, CareersFormAdmin)
