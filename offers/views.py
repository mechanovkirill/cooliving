from collections import defaultdict

from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import DetailView, CreateView, TemplateView
from .models import Offer, Countries, City


class HousingOfferDetailView(DetailView):
    model = Offer
    template_name = 'offers/house_offer_detail.html'
    context_object_name = 'housing_offer'


class HousingOfferCreateView(CreateView):
    model = Offer
    template_name = 'offers/house_offer_create.html'
    fields = '__all__'


class HousingOfferListView(TemplateView):
    template_name = 'offers/housing_offer_list.html'

    CITY_SELECTED = {}
    COUNTRY_SELECTED = {}
    QUERY_PARAMS_DICT = {}

    @staticmethod
    def is_valid_queryparam(param):
        return param != '' and param is not None and param

    def listing_queryparams(self, request, re):
        res = []
        for param, value in self.request.GET.items():
            if str(param).startswith(re):
                if param != '' and param is not None:
                    res.append(value)
        return [v for v in res if v]

    def get_queryset(self):
        qs = Offer.objects.filter(is_active=True).filter(city__city=self.CITY_SELECTED.get('city'))
        gender_of_living = self.request.GET.get('gender_of_living')
        house_type = self.listing_queryparams(self.request, 'house_type')
        sex = self.request.GET.get('sex')
        # number_of_rooms = self.listing_queryparams(self.request, 'n_rooms')
        interior_condition = self.request.GET.get('interior_condition')
        furniture = self.request.GET.get('furniture')
        heating = self.request.GET.get('heating')
        internet_options = self.listing_queryparams(self.request, 'internet_op')
        number_of_living = self.request.GET.get('number_living')
        free_space = self.request.GET.get('freespace')
        min_cost = self.request.GET.get('min_cost')
        max_cost = self.request.GET.get('max_cost')
        min_rental_period = self.request.GET.get('min_rental_period')
        with_kids = self.request.GET.get('with_kids')
        with_animals = self.request.GET.get('with_animals')
        discard_filters = self.request.GET.get('discard_filters')

        if self.is_valid_queryparam(self.request.GET.get('sex')):
            self.QUERY_PARAMS_DICT['Пол|gender'] = self.request.GET.get('sex')
            qs = qs.filter(lodger_desired_sex=self.QUERY_PARAMS_DICT.get('Пол|gender'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Пол|gender')):
            qs = qs.filter(lodger_desired_sex=self.QUERY_PARAMS_DICT.get('Пол|gender'))

        if self.is_valid_queryparam(self.request.GET.get('gender_of_living')):
            self.QUERY_PARAMS_DICT['Проживают|people living'] = self.request.GET.get('gender_of_living')
            qs = qs.filter(sex_of_living_lodgers=self.QUERY_PARAMS_DICT.get('Проживают|people living'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Проживают|people living')):
            qs = qs.filter(sex_of_living_lodgers=self.QUERY_PARAMS_DICT.get('Проживают|people living'))

        if self.is_valid_queryparam(self.request.GET.get('with_kids')):
            self.QUERY_PARAMS_DICT['С детьми|with kids'] = self.request.GET.get('with_kids')
            qs = qs.filter(with_kids=self.QUERY_PARAMS_DICT.get('С детьми|with kids'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('С детьми|with kids')):
            qs = qs.filter(with_kids=self.QUERY_PARAMS_DICT.get('С детьми|with kids'))

        if self.is_valid_queryparam(self.listing_queryparams(self.request, 'house_type')):
            self.QUERY_PARAMS_DICT['Тип жилья|housing type'] = self.listing_queryparams(self.request, 'house_type')
            qs = qs.filter(house_type__in=self.QUERY_PARAMS_DICT.get('Тип жилья|housing type'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Тип жилья|housing type')):
            qs = qs.filter(house_type__in=self.QUERY_PARAMS_DICT.get('Тип жилья|housing type'))

        if self.is_valid_queryparam(self.listing_queryparams(self.request, 'n_rooms')):
            self.QUERY_PARAMS_DICT['Количество комнат|number of rooms'] = self.listing_queryparams(self.request, 'n_rooms')
            qs = qs.filter(number_of_rooms__in=self.QUERY_PARAMS_DICT.get('Количество комнат|number of rooms'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Количество комнат|number of rooms')):
            qs = qs.filter(number_of_rooms__in=self.QUERY_PARAMS_DICT.get('Количество комнат|number of rooms'))

        if self.is_valid_queryparam(self.request.GET.get('interior_condition')):
            self.QUERY_PARAMS_DICT['Отделка|interior'] = self.request.GET.get('interior_condition')
            qs = qs.filter(interior_condition=self.QUERY_PARAMS_DICT.get('Отделка|interior'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Отделка|interior')):
            qs = qs.filter(interior_condition=self.QUERY_PARAMS_DICT.get('Отделка|interior'))

        if self.is_valid_queryparam(self.request.GET.get('furniture')):
            self.QUERY_PARAMS_DICT['Мебель|furniture'] = self.request.GET.get('furniture')
            qs = qs.filter(furniture=self.QUERY_PARAMS_DICT.get('Мебель|furniture'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Мебель|furniture')):
            qs = qs.filter(furniture=self.QUERY_PARAMS_DICT.get('Мебель|furniture'))

        if self.is_valid_queryparam(self.request.GET.get('heating')):
            self.QUERY_PARAMS_DICT['Отопление|heating'] = self.request.GET.get('heating')
            qs = qs.filter(heating=self.QUERY_PARAMS_DICT.get('Отопление|heating'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Отопление|heating')):
            qs = qs.filter(heating=self.QUERY_PARAMS_DICT.get('Отопление|heating'))

        if self.is_valid_queryparam(self.listing_queryparams(self.request, 'internet_op')):
            self.QUERY_PARAMS_DICT['Интернет|internet'] = self.listing_queryparams(self.request, 'internet_op')
            qs = qs.filter(internet__in=self.QUERY_PARAMS_DICT.get('Интернет|internet'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Интернет|internet')):
            qs = qs.filter(internet__in=self.QUERY_PARAMS_DICT.get('Интернет|internet'))

        if self.is_valid_queryparam(self.request.GET.get('number_living')):
            self.QUERY_PARAMS_DICT['Мак.проживающих|Max.lodgers'] = self.request.GET.get('number_living')
            qs = qs.filter(number_of_lodgers__lte=self.QUERY_PARAMS_DICT.get('Мак.проживающих|Max.lodgers'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Мак.проживающих|Max.lodgers')):
            qs = qs.filter(number_of_lodgers__lte=self.QUERY_PARAMS_DICT.get('Мак.проживающих|Max.lodgers'))

        if self.is_valid_queryparam(self.request.GET.get('freespace')):
            self.QUERY_PARAMS_DICT['Свободно мест|free space'] = self.request.GET.get('freespace')
            qs = qs.filter(free_space_for_num_person__lte=self.QUERY_PARAMS_DICT.get('Свободно мест|free space'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Свободно мест|free space')):
            qs = qs.filter(free_space_for_num_person__lte=self.QUERY_PARAMS_DICT.get('Свободно мест|free space'))

        if self.is_valid_queryparam(self.request.GET.get('min_cost')):
            self.QUERY_PARAMS_DICT['Минимальная цена|min. price'] = self.request.GET.get('min_cost')
            qs = qs.filter(cost_per_person__gte=self.QUERY_PARAMS_DICT.get('Свободно мест|free space'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Свободно мест|free space')):
            qs = qs.filter(cost_per_person__gte=self.QUERY_PARAMS_DICT.get('Свободно мест|free space'))

        if self.is_valid_queryparam(min_cost):
            qs = qs.filter(cost_per_person__gte=min_cost)

        if self.is_valid_queryparam(max_cost):
            qs = qs.filter(cost_per_person__lte=max_cost)

        if self.is_valid_queryparam(min_rental_period):
            qs = qs.filter(min_rental_period__lte=min_rental_period)

        if self.is_valid_queryparam(with_animals):
            qs = qs.filter(with_animals=with_animals)

        if self.is_valid_queryparam(discard_filters):
            self.QUERY_PARAMS_DICT.clear()
            qs = Offer.objects.filter(is_active=True).filter(city__city=self.CITY_SELECTED.get('city'))

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = self.request.GET.get('country_select')
        city = self.request.GET.get('city_select')
        placeholder_country = 'Сперва выберите страну | First select a country'
        placeholder_city = ''
        filters_selected = ''
        city_qs = None
        countries = Countries.objects.all()

        if self.is_valid_queryparam(country):
            city_qs = City.objects.filter(country__country=country)
            placeholder_country = f'Выбранная страна | Selected country   {country}'
            placeholder_city = 'Теперь выберите город | Now select a city'
            self.COUNTRY_SELECTED.clear()
            self.CITY_SELECTED.clear()
            self.QUERY_PARAMS_DICT.clear()
            self.COUNTRY_SELECTED['country'] = country

        if self.is_valid_queryparam(city):
            self.CITY_SELECTED.clear()
            self.CITY_SELECTED['city'] = city
            self.QUERY_PARAMS_DICT.clear()

        if self.CITY_SELECTED:
            qs = self.get_queryset()
            paginator = Paginator(qs, 5)
            page = self.request.GET.get('page')
            page_obj = paginator.get_page(page)
            offers_count = qs.count()
            context['offers_count'] = offers_count
            context['page_obj'] = page_obj
            placeholder_city = f'Выбран город | Selected city {self.CITY_SELECTED.get("city")}'
            if self.QUERY_PARAMS_DICT:
                filters_selected = ', '.join(x for x in self.QUERY_PARAMS_DICT.keys())
                print(self.QUERY_PARAMS_DICT)

        if self.COUNTRY_SELECTED:
            city_qs = City.objects.filter(country__country=self.COUNTRY_SELECTED.get('country'))
            placeholder_country = f'Выбрана страна | Selected country {self.COUNTRY_SELECTED.get("country")}'

        context['countries'] = countries
        context['city_qs'] = city_qs
        context['placeholder_country'] = placeholder_country
        context['placeholder_city'] = placeholder_city
        context['filters_selected'] = filters_selected

        return context

