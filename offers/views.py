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
    return [int(v) for v in res if v]


def filters(request):
    gender_of_living = request.GET.get('gender_living_select')
    house_type = listing_queryparams(request, 'house_type')
    sex = request.GET.get('sex')
    number_of_rooms = listing_queryparams(request, 'n_rooms')
    interior_condition = request.GET.get('interior_condition')
    furniture = request.GET.get('furniture-sel')
    heating = request.GET.get('heating-sel')
    internet_options = listing_queryparams(request, 'internet_op')

    qs = Offer.objects.all().filter(city__city=CITY_SELECTED[0])

    if is_valid_queryparam(sex):
        qs = qs.filter(desired_gender=sex)

    if is_valid_queryparam(gender_of_living):
        qs = qs.filter(gender_of_living=gender_of_living)

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
