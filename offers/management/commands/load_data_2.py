from random import randint, choice
from django.core.management.base import BaseCommand
from offers.models import City, Offer
from accounts.models import Account



mocks = ['Жилье 1', 'Жилье 2', 'Жилье 3', 'жилье 4', 'жилье 5', 'Жилье 6', 'Жилье 7']
ch = (True, False)
dist = ('Sarbutalo', 'Раменки', 'Varketili')
SEX = [
        'Женщин | Females',
        'Мужчин | Males',
        'Мужчин и женщин | Men & women',
]
SEX_HOUSE = [
        'Женщины | Females',
        'Мужчины | Males',
        'Мужчины и женщины | Men & women',
        "Никто не живет | No one lives",
    ]
HOUSE_TYPES = [
        'Квартира | Apartment',
        'Дом | House',
        'Комната | Room'
    ]
HEATINGS = [
        'Центральное | Central heating',
        'Электрическое | Electric',
        'Газовое | Gas',
        'Кондиционер | Conditioner',
        'Печное | Stove heating',
        'Отсутствует | No hiating',
        'Другое | Other'
    ]
ROOMS = [
    '1',
    '2',
    '3',
    '4+',
    'Студия | Studio',
]
INTERNET = [
        'Ethernet/ GPON(optic)',
        'ADSL',
        'Отсутствует | No internet',
    ]
INTERIOR = [
        'Новый ремонт | Good interior condition',
        'Без ремонта | Old interior',
        'Требуется ремонт | Repair required',
    ]
FURNITURE = [
    'Полностью | Fully furnished',
    'Частично | Partially furnished',
    'Без мебели | Without furniture',
]
APPLIANCES = [
        'Все необходимое | Necessary',
        'Частично | Partially available',
        'Отсутствует | No appliances',
         'Необходимое и дополнительно | Necessary+'
    ]

photos = ['/media/photos/house_offers/1.jpg',
          '/media/photos/house_offers/2.jpg',
          '/media/photos/house_offers/5fccbca8e1468b36c84fc0b39caf219f.jpg',
          '/media/photos/house_offers/sk_mv.ru_project_Kirpolie_HOME.jpg',
          '/media/photos/house_offers/Без названия.jfif',
          '/media/photos/house_offers/Без названия (1).jfif',
          ]
class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(len(mocks)):
            offer = Offer()
            offer.name = mocks[i]
            offer.user = Account.objects.get(id=1)
            offer.city = City.objects.get(city__exact='Jurm')
            offer.desired_lodgers_gender = randint(1, 3)
            offer.sex_of_now_lodgers = randint(1, 4)
            offer.with_kids = choice(ch)
            offer.district = choice(dist)
            offer.house_type = randint(1, 3)
            offer.number_of_rooms = randint(1, 4)
            offer.interior_condition = randint(1, 3)
            offer.furniture = randint(1, 3)
            offer.appliances = randint(1, 4)
            offer.heating = randint(1, 5)
            offer.internet = randint(1, 3)
            offer.number_of_lodgers = randint(1, 6)
            offer.free_space_for_num_person = randint(1, 4)
            offer.total_cost = randint(100, 1000)
            offer.cost_per_person = randint(50, 500)
            offer.average_utility_bill = randint(10, 150)
            offer.min_rental_period = randint(2, 12)
            offer.separate_room = choice(ch)
            offer.has_balcony = choice(ch)
            offer.has_loggia = choice(ch)
            offer.has_parking = choice(ch)
            offer.transport_nearby = choice(ch)
            offer.with_animals = choice(ch)
            offer.can_smoke = choice(ch)
            offer.contacts = "skdfdsfvkjdnvkjdfvsdf"
            offer.description = 'djfnsclksdjveruhvjnkdbvlkzxckvjb'
            offer.photo_1 = choice(photos)
            offer.photo_2 = choice(photos)
            offer.photo_3 = choice(photos)
            offer.photo_4 = choice(photos)
            offer.save()

        print('finished')
