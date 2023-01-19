from django import forms
from .models import Offer
from django.utils.translation import gettext_lazy as _


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ['city', 'user', 'is_active', 'count_of_views', 'in_favorites']

        labels = {
            'name': _('Writer'),

        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desired_lodgers_gender': forms.Select(attrs={'class': 'form-control'}),
            'sex_of_now_lodgers': forms.Select(attrs={'class': 'form-control'}),
            'with_kids': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'house_type': forms.Select(attrs={'class': 'form-control'}),
            'number_of_rooms': forms.Select(attrs={'class': 'form-control'}),
            'house_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'heating': forms.Select(attrs={'class': 'form-control'}),
            'internet': forms.Select(attrs={'class': 'form-control'}),
            'interior_condition': forms.Select(attrs={'class': 'form-control'}),
            'furniture': forms.Select(attrs={'class': 'form-control'}),
            'appliances': forms.Select(attrs={'class': 'form-control'}),
            'number_of_lodgers': forms.NumberInput(attrs={'class': 'form-control'}),
            'free_space_for_num_person': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_per_person': forms.NumberInput(attrs={'class': 'form-control'}),
            'average_utility_bill': forms.NumberInput(attrs={'class': 'form-control'}),
            'min_rental_period': forms.NumberInput(attrs={'class': 'form-control'}),
            'separate_room': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_balcony': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_loggia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_parking': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'transport_nearby': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'with_animals': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_smoke': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'contacts': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo_1': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_3': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_4': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_area(self):
        area = self.cleaned_data.get('area')
        if area < 20:
            raise forms.ValidationError("Area must be at least 20 sq.m.")
        return area
