from django.shortcuts import render
from .models import Offer, Countries, City

CITY_SELECTED = []


def is_valid_queryparam(param):
    return param != '' and param is not None


def listing_queryparams(request, re):
    res = []
    for param, value in request.GET.items():
        if str(param).startswith(re):
            if param != '' and param is not None:
                res.append(value)
    return [v for v in res if v]


def filters(request):
    gender_of_living = request.GET.get('gender_of_living')
    house_type = listing_queryparams(request, 'house_type')
    sex = request.GET.get('sex')
    number_of_rooms = listing_queryparams(request, 'n_rooms')
    interior_condition = request.GET.get('interior_condition')
    furniture = request.GET.get('furniture')
    heating = request.GET.get('heating')
    internet_options = listing_queryparams(request, 'internet_op')
    number_of_living = request.GET.get('number_living')
    free_space = request.GET.get('freespace')
    min_cost = request.GET.get('min_cost')
    max_cost = request.GET.get('max_cost')
    min_rental_period = request.GET.get('min_rental_period')
    with_animals = request.GET.get('with_animals')
    discard_filters = request.GET.get('discard_filters')

    qs = Offer.objects.all().filter(is_active=True).filter(city__city=CITY_SELECTED[0])

    if is_valid_queryparam(sex):
        qs = qs.filter(lodger_desired_sex=sex)

    if is_valid_queryparam(gender_of_living):
        qs = qs.filter(sex_of_living_lodgers=gender_of_living)

    if house_type:
        qs = qs.filter(house_type__in=house_type)

    if number_of_rooms:
        qs = qs.filter(number_of_rooms__in=number_of_rooms)

    if is_valid_queryparam(interior_condition):
        qs = qs.filter(interior_condition=interior_condition)

    if is_valid_queryparam(furniture):
        qs = qs.filter(furniture=furniture)

    if is_valid_queryparam(heating):
        qs = qs.filter(heating=heating)

    if internet_options:
        qs = qs.filter(internet__in=internet_options)

    if is_valid_queryparam(number_of_living):
        qs = qs.filter(count_of_living__lte=number_of_living)

    if is_valid_queryparam(free_space):
        qs = qs.filter(wanted_quantity_of_person__lte=free_space)

    if is_valid_queryparam(min_cost):
        qs = qs.filter(cost_per_person__gte=min_cost)

    if is_valid_queryparam(max_cost):
        qs = qs.filter(cost_per_person__lte=max_cost)

    if is_valid_queryparam(min_rental_period):
        qs = qs.filter(rental_period__lte=min_rental_period)

    if is_valid_queryparam(with_animals):
        qs = qs.filter(with_animals=with_animals)

    if is_valid_queryparam(discard_filters):
        qs = Offer.objects.all().filter(is_active=True).filter(city__city=CITY_SELECTED[0])

    return qs


def offers(request):
    qs = None
    country = request.GET.get('country_select')
    city = request.GET.get('city_select')
    placeholder_country = 'Сперва выберите страну | First select a country'
    placeholder_city = ''
    city_qs = None
    countries = Countries.objects.all()

    if is_valid_queryparam(country):
        city_qs = City.objects.all().filter(country__country=country)
        placeholder_country = f'Выбранная страна | Selected country   {country}'
        placeholder_city = 'Теперь выберите город | Now select a city'

    if is_valid_queryparam(city):
        CITY_SELECTED.clear()
        CITY_SELECTED.append(city)

    if CITY_SELECTED:
        placeholder_country = ''
        placeholder_city = f'{CITY_SELECTED[0]}'
        qs = filters(request)

    context = {
        'qs': qs,
        'countries': countries,
        'city_qs': city_qs,
        'placeholder_country': placeholder_country,
        'placeholder_city': placeholder_city,
    }

    return render(request, 'offers/house_offers.html', context=context)
