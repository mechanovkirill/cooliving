from django.urls import reverse
from django.core.paginator import Paginator
from django.views.generic import DetailView, CreateView, TemplateView, UpdateView
from .models import Offer, Countries, City
from .forms import OfferForm


class HousingOfferDetailView(DetailView):
    model = Offer
    template_name = 'offers/house_offer_detail.html'
    context_object_name = 'housing_offer'


class OfferCreateView(CreateView):
    model = Offer
    form_class = OfferForm
    template_name = 'offers/offer_form.html'

    def get_context_data(self, **kwargs):
        placeholder_country = 'Выберите страну | Choose country'
        context = super().get_context_data(**kwargs)
        countries = Countries.objects.all()
        cities = ''
        country = self.request.GET.get('country_select')
        if country != '' and not None:
            cities = City.objects.filter(country__country=country)
            placeholder_country = country

        context['countries'] = countries
        context['cities'] = cities
        context['placeholder_country'] = placeholder_country

        return context

    def form_valid(self, form):
        city = City.objects.get(city=self.request.POST.get('city_select'))
        form.instance.user = self.request.user
        form.instance.city = city
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('housing_details', args=[str(self.object.id)])


# class OfferUpdateView(UpdateView):
#     model = Offer
#     form_class = OfferForm
#     template_name = 'offers/offer_form.html'
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('housing_details', args=[str(self.object.id)])


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

        srgg = self.request.GET.get
        sqpdg = self.QUERY_PARAMS_DICT.get

        if self.is_valid_queryparam(srgg('sex')):
            self.QUERY_PARAMS_DICT['Пол|gender'] = srgg('sex')
            qs = qs.filter(desired_lodgers_gender=sqpdg('Пол|gender'))
        elif self.is_valid_queryparam(sqpdg('Пол|gender')):
            qs = qs.filter(desired_lodgers_gender=sqpdg('Пол|gender'))

        if self.is_valid_queryparam(srgg('gender_of_living')):
            self.QUERY_PARAMS_DICT['Проживают|people living'] = srgg('gender_of_living')
            qs = qs.filter(sex_of_now_lodgers=sqpdg('Проживают|people living'))
        elif self.is_valid_queryparam(sqpdg('Проживают|people living')):
            qs = qs.filter(sex_of_now_lodgers=sqpdg('Проживают|people living'))

        if self.is_valid_queryparam(srgg('with_kids')):
            self.QUERY_PARAMS_DICT['С детьми|with kids'] = srgg('with_kids')
            qs = qs.filter(with_kids=sqpdg('С детьми|with kids'))
        elif self.is_valid_queryparam(sqpdg('С детьми|with kids')):
            qs = qs.filter(with_kids=sqpdg('С детьми|with kids'))

        if self.is_valid_queryparam(srgg('district')):
            self.QUERY_PARAMS_DICT['Район | District'] = srgg('district')
            qs = qs.filter(district__icontains=sqpdg('Район | District'))
        elif self.is_valid_queryparam(sqpdg('Район | District')):
            qs = qs.filter(district__icontains=sqpdg('Район | District'))

        if self.is_valid_queryparam(self.listing_queryparams(self.request, 'house_type')):
            self.QUERY_PARAMS_DICT['Тип жилья|housing type'] = self.listing_queryparams(self.request, 'house_type')
            qs = qs.filter(house_type__in=sqpdg('Тип жилья|housing type'))
        elif self.is_valid_queryparam(sqpdg('Тип жилья|housing type')):
            qs = qs.filter(house_type__in=sqpdg('Тип жилья|housing type'))

        if self.is_valid_queryparam(self.listing_queryparams(self.request, 'n_rooms')):
            self.QUERY_PARAMS_DICT['Количество комнат|number of rooms'] = self.listing_queryparams(self.request, 'n_rooms')
            qs = qs.filter(number_of_rooms__in=self.QUERY_PARAMS_DICT.get('Количество комнат|number of rooms'))
        elif self.is_valid_queryparam(self.QUERY_PARAMS_DICT.get('Количество комнат|number of rooms')):
            qs = qs.filter(number_of_rooms__in=self.QUERY_PARAMS_DICT.get('Количество комнат|number of rooms'))

        if self.is_valid_queryparam(srgg('interior_condition')):
            self.QUERY_PARAMS_DICT['Отделка|interior'] = srgg('interior_condition')
            qs = qs.filter(interior_condition=sqpdg('Отделка|interior'))
        elif self.is_valid_queryparam(sqpdg('Отделка|interior')):
            qs = qs.filter(interior_condition=sqpdg('Отделка|interior'))

        if self.is_valid_queryparam(srgg('furniture')):
            self.QUERY_PARAMS_DICT['Мебель|furniture'] = srgg('furniture')
            qs = qs.filter(furniture=sqpdg('Мебель|furniture'))
        elif self.is_valid_queryparam(sqpdg('Мебель|furniture')):
            qs = qs.filter(furniture=sqpdg('Мебель|furniture'))

        if self.is_valid_queryparam(srgg('appliances')):
            self.QUERY_PARAMS_DICT['Бытовая техника|Appliances'] = srgg('appliances')
            qs = qs.filter(furniture=sqpdg('Бытовая техника|Appliances'))
        elif self.is_valid_queryparam(sqpdg('Бытовая техника|Appliances')):
            qs = qs.filter(furniture=sqpdg('Бытовая техника|Appliances'))

        if self.is_valid_queryparam(srgg('heating')):
            self.QUERY_PARAMS_DICT['Отопление|heating'] = srgg('heating')
            qs = qs.filter(heating=sqpdg('Отопление|heating'))
        elif self.is_valid_queryparam(sqpdg('Отопление|heating')):
            qs = qs.filter(heating=sqpdg('Отопление|heating'))

        if self.is_valid_queryparam(self.listing_queryparams(self.request, 'internet_op')):
            self.QUERY_PARAMS_DICT['Интернет|internet'] = self.listing_queryparams(self.request, 'internet_op')
            qs = qs.filter(internet__in=sqpdg('Интернет|internet'))
        elif self.is_valid_queryparam(sqpdg('Интернет|internet')):
            qs = qs.filter(internet__in=sqpdg('Интернет|internet'))

        if self.is_valid_queryparam(srgg('number_living')):
            self.QUERY_PARAMS_DICT['Макc.проживающих|Max.lodgers'] = srgg('number_living')
            qs = qs.filter(number_of_lodgers__lte=sqpdg('Макc.проживающих|Max.lodgers'))
        elif self.is_valid_queryparam(sqpdg('Макc.проживающих|Max.lodgers')):
            qs = qs.filter(number_of_lodgers__lte=sqpdg('Макc.проживающих|Max.lodgers'))

        if self.is_valid_queryparam(srgg('freespace')):
            self.QUERY_PARAMS_DICT['Свободно мест|free space'] = srgg('freespace')
            qs = qs.filter(free_space_for_num_person__lte=sqpdg('Свободно мест|free space'))
        elif self.is_valid_queryparam(sqpdg('Свободно мест|free space')):
            qs = qs.filter(free_space_for_num_person__lte=sqpdg('Свободно мест|free space'))

        if self.is_valid_queryparam(srgg('min_cost')):
            self.QUERY_PARAMS_DICT['Минимальная цена|min. price'] = srgg('min_cost')
            qs = qs.filter(cost_per_person__gte=sqpdg('Минимальная цена|min. price'))
        elif self.is_valid_queryparam(sqpdg('Минимальная цена|min. price')):
            qs = qs.filter(cost_per_person__gte=sqpdg('Минимальная цена|min. price'))

        if self.is_valid_queryparam(srgg('max_cost')):
            self.QUERY_PARAMS_DICT['Минимальная цена|min. price'] = srgg('max_cost')
            qs = qs.filter(cost_per_person__lte=sqpdg('Свободно мест|free space'))
        elif self.is_valid_queryparam(sqpdg('Свободно мест|free space')):
            qs = qs.filter(cost_per_person__lte=sqpdg('Свободно мест|free space'))

        if self.is_valid_queryparam(srgg('min_rental_period')):
            self.QUERY_PARAMS_DICT['Период аренды|rental period'] = srgg('min_rental_period')
            qs = qs.filter(min_rental_period__lte=sqpdg('Период аренды|rental period'))
        elif self.is_valid_queryparam(sqpdg('Период аренды|rental period')):
            qs = qs.filter(min_rental_period__lte=sqpdg('Период аренды|rental period'))

        if self.is_valid_queryparam(srgg('separate_room')):
            self.QUERY_PARAMS_DICT['Отдельная комната|has separate room'] = srgg('separate_room')
            qs = qs.filter(separate_room=sqpdg('Отдельная комната|has separate room'))
        elif self.is_valid_queryparam(sqpdg('Отдельная комната|has separate room')):
            qs = qs.filter(separate_room=sqpdg('Отдельная комната|has separate room'))

        if self.is_valid_queryparam(srgg('has_balcony')):
            self.QUERY_PARAMS_DICT['Есть балкон|Has balcony'] = srgg('has_balcony')
            qs = qs.filter(has_balcony=sqpdg('Есть балкон|Has balcony'))
        elif self.is_valid_queryparam(sqpdg('Есть балкон|Has balcony')):
            qs = qs.filter(has_balcony=sqpdg('Есть балкон|Has balcony'))

        if self.is_valid_queryparam(srgg('has_loggia')):
            self.QUERY_PARAMS_DICT['Есть лоджия|Has loggia'] = srgg('has_loggia')
            qs = qs.filter(has_loggia=sqpdg('Есть лоджия|Has loggia'))
        elif self.is_valid_queryparam(sqpdg('Есть лоджия|Has loggia')):
            qs = qs.filter(has_loggia=sqpdg('Есть лоджия|Has loggia'))

        if self.is_valid_queryparam(srgg('has_parking')):
            self.QUERY_PARAMS_DICT['Есть парковка|Has parking'] = srgg('has_parking')
            qs = qs.filter(has_parking=sqpdg('Есть парковка|Has parking'))
        elif self.is_valid_queryparam(sqpdg('Есть парковка|Has parking')):
            qs = qs.filter(has_parking=sqpdg('Есть парковка|Has parking'))

        if self.is_valid_queryparam(srgg('transport_nearby')):
            self.QUERY_PARAMS_DICT['Транспорт рядом|Transport nearby'] = srgg('transport_nearby')
            qs = qs.filter(transport_nearby=sqpdg('Транспорт рядом|Transport nearby'))
        elif self.is_valid_queryparam(sqpdg('Транспорт рядом|Transport nearby')):
            qs = qs.filter(transport_nearby=sqpdg('Транспорт рядом|Transport nearby'))

        if self.is_valid_queryparam(srgg('with_animals')):
            self.QUERY_PARAMS_DICT['С животными|with animals'] = srgg('with_animals')
            qs = qs.filter(with_animals=sqpdg('С животными|with animals'))
        elif self.is_valid_queryparam(sqpdg('С животными|with animals')):
            qs = qs.filter(with_animals=sqpdg('С животными|with animals'))

        if self.is_valid_queryparam(srgg('can_smoke')):
            self.QUERY_PARAMS_DICT['Можно курить|Smoking allowed'] = srgg('can_smoke')
            qs = qs.filter(can_smoke=sqpdg('Можно курить|Smoking allowed'))
        elif self.is_valid_queryparam(sqpdg('Можно курить|Smoking allowed')):
            qs = qs.filter(can_smoke=sqpdg('Можно курить|Smoking allowed'))

        if self.is_valid_queryparam(self.request.GET.get('discard_filters')):
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

