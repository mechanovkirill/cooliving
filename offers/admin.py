from django.contrib import admin
from .models import Offer, City, Countries


class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'city', 'desired_lodgers_gender', 'sex_of_now_lodgers', 'house_type',
        'number_of_rooms', 'interior_condition', 'heating', 'number_of_lodgers', 'internet',
        'furniture', 'appliances', 'created_date', 'modified_date', 'free_space_for_num_person', 'total_cost',
        'cost_per_person', 'min_rental_period', 'with_animals', 'with_kids', 'separate_room', 'has_balcony',
        'has_loggia', 'has_parking', 'can_smoke', 'is_active',
    )


admin.site.register(Offer, OfferAdmin)
admin.site.register(City)
admin.site.register(Countries)
