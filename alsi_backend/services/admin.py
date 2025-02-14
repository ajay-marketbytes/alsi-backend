from django.contrib import admin
from .models import Services, Subcategory, Card

class CardInline(admin.TabularInline):
    model = Card
    extra = 1


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_title', 'link_url')
    search_fields = ('title', 'service_title', 'link_url')
    inlines = [SubcategoryInline]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text_color', 'enable_fill_empty_cards', 'service')
    search_fields = ('title', 'service__title')
    inlines = [CardInline]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory')
    search_fields = ('title', 'subcategory__title')
