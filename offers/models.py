from django.db import models
from accounts.models import Account

SEX = [
    (1, 'Женщины | Females'),
    (2, 'Мужчины | Males'),
    (3, 'Смешанно | Mixed'),
    (4, "Не важно | Doesn't matter"),
]

HOUSE_TYPES = [
    (1, 'Квартира | Apartment'),
    (2, 'Дом | House'),
    (3, 'Комната | Room'),
]

HEATINGS = [
    (1, 'Центральное | Central heating'),
    (2, 'Электрическое | Electric'),
    (3, 'Газовое | Gas'),
    (4, 'Кондиционер | Conditioner'),
    (6, 'Печное | Stove heating'),
    (5, 'Отсутствует | No hiating'),
    (7, 'Другое | Other'),
]

ROOMS = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4+'),
]

INTERNET = [
    (1, 'Ithernet/ GPON(optic)'),
    (2, 'ADSL'),
    (3, 'Отсутствует | '),
]

INTERIOR = [
    (1, 'Новый ремонт | '),
    (2, 'Без ремонта | '),
]

FURNITURE = [
    (1, 'Полностью | '),
    (2, 'Частично | '),
    (3, 'Без мебели | '),
]


class Countries(models.Model):
    country = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.country


class City(models.Model):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    city = models.CharField(max_length=64)

    def __str__(self):
        return self.city


class Offer(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=256, unique=True, allow_unicode=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.CharField(max_length=50, null=True, blank=True)
    gender_of_living = models.PositiveSmallIntegerField(choices=SEX)
    desired_gender = models.PositiveSmallIntegerField(choices=SEX)
    house_type = models.PositiveSmallIntegerField(choices=HOUSE_TYPES)
    number_of_rooms = models.PositiveSmallIntegerField(choices=ROOMS)
    heating = models.PositiveSmallIntegerField(choices=HEATINGS)
    internet = models.PositiveSmallIntegerField(choices=INTERNET)
    interior_condition = models.PositiveSmallIntegerField(choices=INTERIOR)
    furniture = models.PositiveSmallIntegerField(choices=FURNITURE)
    count_of_living = models.PositiveSmallIntegerField()
    wanted_quantity_of_person = models.PositiveSmallIntegerField()
    total_cost = models.FloatField(max_length=10)
    cost_per_person = models.FloatField(max_length=10)
    rental_period = models.PositiveSmallIntegerField()
    with_animals = models.BooleanField(default=False)
    contacts = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/house_offers', max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class OfferGallery(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, default=None)
    photo = models.ImageField(upload_to='photos/house_offers', max_length=254)
