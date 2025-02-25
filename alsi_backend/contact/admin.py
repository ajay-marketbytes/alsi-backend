from django.contrib import admin
from .models import ContactBanner, ContactForm

# Register ContactBanner model
@admin.register(ContactBanner)
class ContactBannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Columns to display in the admin list view
    search_fields = ('title',)  # Add search functionality for title
    list_per_page = 25  # Pagination

# Register ContactForm model
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'submitted_at')  # Columns to display
    list_filter = ('submitted_at',)  # Add filter by submission date
    search_fields = ('name', 'email', 'phone')  # Search by these fields
    date_hierarchy = 'submitted_at'  # Add date-based navigation
    list_per_page = 25  # Pagination
    
    # Optional: Make some fields read-only in the detail view
    readonly_fields = ('submitted_at', 'referer_url', 'submitted_url')

# If you prefer the simpler registration method, you could just use:
# admin.site.register(ContactBanner)
# admin.site.register(ContactForm)