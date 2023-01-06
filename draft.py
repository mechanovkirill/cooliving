# from django.db.models import Q
# from django.shortcuts import render
# from .models import Offer, OfferGallery, Countries, City
#
# CITY_SELECTED = []
#
#
# def is_valid_queryparam(param):
#     return param != '' and param is not None
#
#
# def filters(request):
#
#     return qs
#
#
# def offers(request):
#     placeholder_country = 'Сперва выберите страну | First select a country'
#     placeholder_city = ''
#     qs = None
#     city_qs = None
#     countries = Countries.objects.all()
#     # get requests
#     country = request.GET.get('country_select')
#     city = request.GET.get('city_select')
#     gender_of_living = request.GET.get('gender_living_select')
#     house_type_1 = request.GET.get('house_type_1')
#     house_type_2 = request.GET.get('house_type_2')
#     house_type_3 = request.GET.get('house_type_3')
#     house_type_ = [house_type_1, house_type_2, house_type_3]
#     house_type = [int(v) for v in house_type_ if v]
#     sex = request.GET.get('sex')
#     n_rooms_1 = request.GET.get('n_rooms_1')
#     n_rooms_2 = request.GET.get('n_rooms_2')
#     n_rooms_3 = request.GET.get('n_rooms_3')
#     n_rooms_4 = request.GET.get('n_rooms_4')
#     n_rooms_ = [n_rooms_1, n_rooms_2, n_rooms_3, n_rooms_4]
#     number_of_rooms = [int(v) for v in n_rooms_ if v]
#     # end get requests
#
#     if is_valid_queryparam(country):
#         city_qs = City.objects.all().filter(country__country=country)
#         placeholder_country = f'Выбранная страна | Selected country   {country}'
#         placeholder_city = 'Теперь выберите город | Now select a city'
#
#     if is_valid_queryparam(city):
#         CITY_SELECTED.clear()
#         CITY_SELECTED.append(city)
#
#     if CITY_SELECTED:
#         placeholder_country = ''
#         placeholder_city = f'{CITY_SELECTED[0]}'
#         qs = Offer.objects.all().filter(city__city=CITY_SELECTED[0])
#
#         if is_valid_queryparam(sex):
#             qs = qs.filter(desired_gender=sex)
#
#         if is_valid_queryparam(gender_of_living):
#             qs = qs.filter(gender_of_living=gender_of_living)
#
#         if house_type:
#             qs = qs.filter(house_type__in=house_type)
#
#         if number_of_rooms:
#             qs = qs.filter(number_of_rooms__in=number_of_rooms)
#
#         return qs
#
#     context = {
#         'qs': qs,
#         'countries': countries,
#         'city_qs': city_qs,
#         'placeholder_country': placeholder_country,
#         'placeholder_city': placeholder_city,
#     }
#
#     return render(request, 'offers/house_offers.html', context=context)
