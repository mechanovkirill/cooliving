import django_filters
from .models import Offer, ROOMS
from django import forms


class OfferFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='istartswith')
    number_of_rooms = django_filters.MultipleChoiceFilter(choices=ROOMS, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Offer
        fields = ['city', 'number_of_rooms']
