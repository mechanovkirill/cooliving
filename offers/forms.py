from django import forms
from .models import Offer
from django.utils.translation import gettext_lazy as _


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ['city', 'user', 'is_active', 'count_of_views', 'in_favorites',]

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
            # 'city': forms.Select(attrs={'class': 'form-control'}),
            'lodger_desired_sex': forms.Select(attrs={'class': 'form-control'}),
            'sex_of_living_lodgers': forms.Select(attrs={'class': 'form-control'}),
            'with_kids': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'house_type': forms.Select(attrs={'class': 'form-control'}),
            'number_of_rooms': forms.Select(attrs={'class': 'form-control'}),
            'house_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'heating': forms.Select(attrs={'class': 'form-control'}),
            'internet': forms.Select(attrs={'class': 'form-control'}),
            'interior_condition': forms.Select(attrs={'class': 'form-control'}),
            'furniture': forms.Select(attrs={'class': 'form-control'}),
            'appliances': forms.Select(attrs={'class': 'form-control'}),
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
