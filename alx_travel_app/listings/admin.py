from django.contrib import admin
from .models import TravelListing

@admin.register(TravelListing)
class TravelListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'available_from', 'available_to', 'is_active')
    list_filter = ('is_active', 'location')
    search_fields = ('title', 'location')
