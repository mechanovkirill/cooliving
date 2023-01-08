import json
import os
from django.core.management.base import BaseCommand
from coliving.settings import BASE_DIR
from offers.models import City, Countries

filename = os.path.join(BASE_DIR, 'data/cities.json')


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(filename, 'r') as json_file:
            data = json.load(json_file)

            control = []
            for row in data:
                if row['country_name'] in control:
                    continue
                else:
                    country_tuple = Countries()
                    country_tuple.country = row['country_name']
                    country_tuple.save()
                    control.append(row['country_name'])
            for row in data:
                cntry = Countries.objects.get(country=row['country_name'])
                print(cntry)
                cities_tuple = City()
                cities_tuple.city = row['name']
                cities_tuple.country = cntry
                cities_tuple.save()

        print('finished')

