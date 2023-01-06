import json
import os
from random import randint, choice

from django.core.management.base import BaseCommand
from coliving.settings import BASE_DIR
from offers.models import City, Countries, Offer
from accounts.models import Account

filename = os.path.join(BASE_DIR, 'data/cities.json')


# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         with open(filename, 'r') as json_file:
#             data = json.load(json_file)
#
#             control = []
#             for row in data:
#                 if row['country_name'] in control:
#                     continue
#                 else:
#                     country_tuple = Countries()
#                     country_tuple.country = row['country_name']
#                     country_tuple.save()
#                     control.append(row['country_name'])
#             for row in data:
#                 cntry = Countries.objects.get(country=row['country_name'])
#                 print(cntry)
#                 cities_tuple = City()
#                 cities_tuple.city = row['name']
#                 cities_tuple.country = cntry
#                 cities_tuple.save()
#
#         print('finished')


mocks = ['Жилье 1', 'Жилье 2', 'Жилье 3', 'жилье 4', 'жилье 5', 'Жилье 6']
ch = (True, False)

class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(len(mocks)):
            offer = Offer()
            offer.name = mocks[i]
            offer.user = Account.objects.get(id=1)
            offer.slug = mocks[i].lower()
            offer.city = City.objects.get(city__exact='Jurm')
            offer.gender_of_living = randint(1, 3)
            offer.desired_gender = randint(1, 3)
            offer.house_type = randint(1, 3)
            offer.number_of_rooms = randint(1, 3)
            offer.heating = randint(1, 3)
            offer.internet = randint(1, 3)
            offer.interior_condition = randint(1, 2)
            offer.furniture = randint(1, 3)
            offer.count_of_living = randint(1, 3)
            offer.wanted_quantity_of_person = randint(1, 3)
            offer.total_cost = randint(100, 600)
            offer.cost_per_person = randint(100, 600)
            offer.rental_period = randint(3, 12)
            offer.with_animals = choice(ch)
            offer.contacts = "skdfdsfvkjdnvkjdfvsdf"
            offer.description = 'djfnsclksdjveruhvjnkdbvlkzxckvjb'
            offer.save()

        print('finished')
