from django.views.generic import DetailView, CreateView, ListView
from .models import Offer, Countries, City
from django import template
from django.core.paginator import Paginator

class HousingOfferDetailView(DetailView):
    model = Offer
    template_name = 'offers/house_offer_detail.html'
    context_object_name = 'housing_offer'


class HousingOfferCreateView(CreateView):
    model = Offer
    template_name = 'offers/house_offer_create.html'
    fields = '__all__'


class HousingOfferListView(ListView):
    paginate_by = 5
    model = Offer
    template_name = 'offers/housing_offer_list.html'

    CITY_SELECTED = []
    COUNTRY_SELECTED = []

    @staticmethod
    def is_valid_queryparam(param):
        return param != '' and param is not None

    def listing_queryparams(self, request, re):
        res = []
        for param, value in self.request.GET.items():
            if str(param).startswith(re):
                if param != '' and param is not None:
                    res.append(value)
        return [v for v in res if v]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.CITY_SELECTED:
            qs = Offer.objects.filter(is_active=True).filter(city__city=self.CITY_SELECTED[0])

        gender_of_living = self.request.GET.get('gender_of_living')
        house_type = self.listing_queryparams(self.request, 'house_type')
        sex = self.request.GET.get('sex')
        number_of_rooms = self.listing_queryparams(self.request, 'n_rooms')
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

        if self.is_valid_queryparam(sex):
            qs = qs.filter(lodger_desired_sex=sex)

        if self.is_valid_queryparam(gender_of_living):
            qs = qs.filter(sex_of_living_lodgers=gender_of_living)

        if self.is_valid_queryparam(with_kids):
            qs = qs.filter(with_kids=with_kids)

        if house_type:
            qs = qs.filter(house_type__in=house_type)

        if number_of_rooms:
            qs = qs.filter(number_of_rooms__in=number_of_rooms)

        if self.is_valid_queryparam(interior_condition):
            qs = qs.filter(interior_condition=interior_condition)

        if self.is_valid_queryparam(furniture):
            qs = qs.filter(furniture=furniture)

        if self.is_valid_queryparam(heating):
            qs = qs.filter(heating=heating)

        if internet_options:
            qs = qs.filter(internet__in=internet_options)

        if self.is_valid_queryparam(number_of_living):
            qs = qs.filter(number_of_lodgers__lte=number_of_living)

        if self.is_valid_queryparam(free_space):
            qs = qs.filter(free_space_for_num_person__lte=free_space)

        if self.is_valid_queryparam(min_cost):
            qs = qs.filter(cost_per_person__gte=min_cost)

        if self.is_valid_queryparam(max_cost):
            qs = qs.filter(cost_per_person__lte=max_cost)

        if self.is_valid_queryparam(min_rental_period):
            qs = qs.filter(min_rental_period__lte=min_rental_period)

        if self.is_valid_queryparam(with_animals):
            qs = qs.filter(with_animals=with_animals)

        if self.is_valid_queryparam(discard_filters):
            qs = Offer.objects.filter(is_active=True).filter(city__city=self.CITY_SELECTED[0])

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        country = self.request.GET.get('country_select')
        city = self.request.GET.get('city_select')
        placeholder_country = 'Сперва выберите страну | First select a country'
        placeholder_city = ''
        already_hint = ''
        city_qs = None
        countries = Countries.objects.all()

        if self.is_valid_queryparam(country):
            city_qs = City.objects.all().filter(country__country=country)
            placeholder_country = f'Выбранная страна | Selected country   {country}'
            placeholder_city = 'Теперь выберите город | Now select a city'
            self.COUNTRY_SELECTED.clear()
            self.COUNTRY_SELECTED.append(country)

        if self.is_valid_queryparam(city):
            self.CITY_SELECTED.clear()
            self.CITY_SELECTED.append(city)

        if self.COUNTRY_SELECTED and self.CITY_SELECTED:
            placeholder_country = f'Выбрана страна | Selected country {self.COUNTRY_SELECTED[0]}'
            placeholder_city = f'Выбран город | Selected city {self.CITY_SELECTED[0]}'
            already_hint = ''

        # 'page_obj' = page_obj
        context['countries'] = countries
        context['city_qs'] = city_qs
        context['placeholder_country'] = placeholder_country
        context['placeholder_city'] = placeholder_city
        context['already_hint'] = already_hint

        return context

