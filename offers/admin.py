from django.contrib import admin
from .models import Offer, OfferGallery, City, Countries
import admin_thumbnails


@admin_thumbnails.thumbnail('photo')
class OfferGalleryInline(admin.TabularInline):
    model = OfferGallery
    extra = 1


class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'city', 'desired_gender', 'gender_of_living', 'house_type',
        'number_of_rooms', 'interior_condition', 'heating', 'count_of_living', 'internet',
        'furniture', 'created_date', 'modified_date', 'wanted_quantity_of_person', 'total_cost',
        'cost_per_person', 'rental_period', 'with_animals',
    )
    prepopulated_fields = {'slug': ('name',)}
    inlines = [OfferGalleryInline]


admin.site.register(Offer, OfferAdmin)
admin.site.register(City)
admin.site.register(Countries)
