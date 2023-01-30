from django import forms
from django.forms.renderers import TemplatesSetting
from django.forms.utils import ErrorList
from .models import Offer
from django.utils.translation import gettext_lazy as _


class CustomErrorList(ErrorList):
    def __init__(self, initlist=None, error_class=None, renderer=None):
        super().__init__(initlist, error_class="list-group", renderer=TemplatesSetting())

    template_name = "forms/errors/default.html"
    template_name_text = "forms/text.txt"
    template_name_ul = "forms/errors/ul.html"


class OfferForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_class = CustomErrorList

    class Meta:
        model = Offer
        exclude = ['city', 'user', 'is_active', 'count_of_views', 'in_favorites']

        labels = {
            'name': _('Заголовок | Title'),
            'desired_lodgers_gender': _('Сдается для | Who are you looking for?'),
            'sex_of_now_lodgers': _('Сейчас живут | Gender of current tenants'),
            'with_kids': _('Можно с детьми | Children allowed'),
            'district': _('Район | District'),
            'house_type': _('Тип жилья | Housing type'),
            'number_of_rooms': _('Количество комнат | Number of rooms'),
            'house_area': _('Площадь помещения | Area'),
            'heating': _('Отопление | Heating'),
            'internet': _('Интернет | Internet'),
            'interior_condition': _('Состояние отделки | Interior condition'),
            'furniture': _('Наличие мебели | Availability of furniture'),
            'appliances': _('Наличие бытовой техники | Availability of appliances'),
            'number_of_lodgers': _('Жилье вмещает жильцов | Maximum number of lodgers'),
            'free_space_for_num_person': _('Свободно мест | Free space for lodgers'),
            'total_cost': _('Полная стоимость аренды помещения | Total rental amount'),
            'cost_per_person': _('Сумма аренды на человека | Rental amount per person'),
            'average_utility_bill': _('Средняя стоимость коммунальных услуг | Average utility bill'),
            'min_rental_period': _('Минимальный период аренды | Minimal rental period'),
            'separate_room': _('Отдельная комната | Separate room'),
            'has_balcony': _('Есть балкон | Has balcony'),
            'has_loggia': _('Есть лоджия | Has loggia'),
            'has_parking': _('Есть парковка | Has parking'),
            'transport_nearby': _('Общественный транспорт рядом | Public transport nearby'),
            'with_animals': _('Можно с животными | Animals allowed'),
            'can_smoke': _('Можно курить | Smoking allowed'),
            'contacts': _('Контакты для обратной связи | Contacts for feedback'),
            'description': _('Описание | Description'),
            'photo_1': _('Фотографии | Photos'),
            'photo_2': _(''),
            'photo_3': _(''),
            'photo_4': _(''),
        }

        help_texts = {
            'name': _('<small class="text-muted">Кратко опишите предложение. Не более 100 символов. '
                      'Create useful title. No more than 100 characters.</small>'),
            'desired_lodgers_gender': _('<small class="text-muted">Выберите какого пола людей вы ищите. '
                                        'Choose what gender of people you are looking for.</small>'),
            'sex_of_now_lodgers': _('<small class="text-muted">Выберите пол людей проживающих сейчас '
                                    'в предлагаемом жилье. Select the gender of people currently '
                                    'living in the proposed housing.</small>'),
            'district': _('<small class="text-muted">Не более 50 символов. No more than 50 characters.</small>'),
            'house_area': _('<small class="text-muted">Единица измерения - квадратный метр. '
                            'The unit of measurement is a square meter.</small>'),
            'number_of_lodgers': _('<small class="text-muted">'
                                   'На проживание какого количества жильцов '
                                   'рассчитано жилье? '
                                   'How many residents can the accommodation accommodate?</small>'),
            'free_space_for_num_person': _('<small class="text-muted">'
                                           'Сколько ещё человек вы ищите? '
                                           'How many more people are you looking for?</small>'),
            'total_cost': _('<small class="text-muted">Сумма аренды за месяц '
                            'в долларах США. '
                            'Amount of rent per month in US dollars.</small>'),
            'cost_per_person': _('<small class="text-muted">'
                                 'Сумма аренды за месяц на одного жильца в долларах США. '
                                 'Monthly rent per tenant in US dollars.</small>'),
            'average_utility_bill': _('<small class="text-muted">'
                                      'Средняя стоимость коммунальных услуг в месяц в долларах США. '
                                      'Average cost of utilities per month in USD.</small>'),
            'min_rental_period': _('<small class="text-muted">'
                                   'Минимальный возможный срок аренды в месяцах. '
                                   'The minimum possible rental period in months.</small>'),
            'contacts': _('<small class="text-muted">Укажите удобные для вас контакты для связи. Имейте ввиду, '
                          'что контакты будут находиться в открытом доступе. Не более 128 символов. '
                          'Specify the contacts convenient for you for communication. '
                          'Keep in mind that contacts will be in the public domain. '
                          'No more than 128 characters.</small>'),
            'description': _('<small class="text-muted">Не более 1000 символов. '
                             'No more than 1000 characters.</small>'),
            'photo_4': _('<small class="text-muted"></small>'),
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the text'}),
            'desired_lodgers_gender': forms.Select(attrs={'class': 'form-control'}),
            'sex_of_now_lodgers': forms.Select(attrs={'class': 'form-control'}),
            'with_kids': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the text'}),
            'house_type': forms.Select(attrs={'class': 'form-control'}),
            'number_of_rooms': forms.Select(attrs={'class': 'form-control'}),
            'house_area': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type the number in digits | Введите число цифрами'
            }),
            'heating': forms.Select(attrs={'class': 'form-control'}),
            'internet': forms.Select(attrs={'class': 'form-control'}),
            'interior_condition': forms.Select(attrs={'class': 'form-control'}),
            'furniture': forms.Select(attrs={'class': 'form-control'}),
            'appliances': forms.Select(attrs={'class': 'form-control'}),
            'number_of_lodgers': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type the number in digits | Введите число цифрами'
            }),
            'free_space_for_num_person': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type the number in digits | Введите число цифрами'
            }),
            'total_cost': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type the number in digits | Введите число цифрами'
            }),
            'cost_per_person': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type the number in digits | Введите число цифрами'
            }),
            'average_utility_bill': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type the number in digits | Введите число цифрами'
            }),
            'min_rental_period': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type the number in digits | Введите число цифрами'
            }),
            'separate_room': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_balcony': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_loggia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_parking': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'transport_nearby': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'with_animals': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_smoke': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'contacts': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type the text'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type the text'
            }),
            'photo_1': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_3': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_4': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) <= 2:
            raise forms.ValidationError(
                "Title must be at least 2 characters long. Заголовок должен быть длиннее 2 символов"
            )
        if len(name) > 100:
            raise forms.ValidationError(
                "The title should be no more than 100 characters long. "
                "Длина заголовка должна быть не более 100 символов."
            )
        return name

    def clean_contacts(self):
        contacts = self.cleaned_data.get('contacts')
        if len(contacts) <= 2:
            raise forms.ValidationError(
                "Contacts must be at least 2 characters long. Длина контактов должна быть длиннее 2 символов"
            )
        if len(contacts) > 128:
            raise forms.ValidationError(
                "The contacts should be no more than 128 characters long. "
                "Длина контактов должна быть не более 128 символов."
            )
        return contacts

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise forms.ValidationError(
                "Description must be at least 10 characters long. Описание должно быть длиннее 10 символов"
            )
        if len(description) > 1000:
            raise forms.ValidationError(
                "The Description should be no more than 1000 characters long. "
                "Длина описания должна быть не более 1000 символов."
            )
        return description

    def clean_district(self):
        district = self.cleaned_data.get('district')
        if district and len(district) > 50:
            raise forms.ValidationError(
                "The district name should be no more than 50 characters long. "
                "Наименование района должно быть не длиннее 50 символов."
            )
        return district

    def clean_house_area(self):
        house_area = self.cleaned_data.get('house_area')
        if house_area < 5:
            raise forms.ValidationError(
                "Area must be at least 5 sq.m. Площадь помещения должна быть более 5 кв. метров"
            )
        return house_area

    def clean_number_of_lodgers(self):
        number_of_lodgers = self.cleaned_data.get('number_of_lodgers')
        if number_of_lodgers < 1:
            raise forms.ValidationError(
                "Количество жильцов не может быть меньше 1. The number of tenants cannot be less than 1."
            )
        if number_of_lodgers > 500:
            raise forms.ValidationError(
                "Количество жильцов едва ли может превышать 500, возможно вы ошиблись? "
                "The number of tenants can hardly exceed 500, perhaps you are mistaken?"
            )
        return number_of_lodgers

    def clean_free_space_for_num_person(self):
        free_space_for_num_person = self.cleaned_data.get('free_space_for_num_person')
        if free_space_for_num_person < 1:
            raise forms.ValidationError(
                "Количество жильцов не может быть меньше 1. The number of tenants cannot be less than 1."
            )
        if free_space_for_num_person > 500:
            raise forms.ValidationError(
                "Количество жильцов едва ли может превышать 500, возможно вы ошиблись? "
                "The number of tenants can hardly exceed 500, perhaps you are mistaken?"
            )
        return free_space_for_num_person

    def clean_total_cost(self):
        total_cost = self.cleaned_data.get('total_cost')
        if total_cost < 1:
            raise forms.ValidationError(
                "Стоимость аренды не может быть меньше единицы. The rental price cannot be less than one."
            )
        return total_cost

    def clean_cost_per_person(self):
        cost_per_person = self.cleaned_data.get('cost_per_person')
        if cost_per_person < 1:
            raise forms.ValidationError(
                "Стоимость аренды не может быть меньше единицы. The rental price cannot be less than one."
            )
        return cost_per_person

    def clean_min_rental_period(self):
        min_rental_period = self.cleaned_data.get('min_rental_period')
        if min_rental_period < 1:
            raise forms.ValidationError(
                "Минимальный срок аренды не может быть меньше одного месяца. "
                "The minimum rental period cannot be less than one month."
            )
        return min_rental_period

