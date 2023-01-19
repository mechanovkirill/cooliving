from django.db import models
from accounts.models import Account
from django.shortcuts import reverse


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

    SEX = [
        ('1', 'Женщин | Females'),
        ('2', 'Мужчин | Males'),
        ('3', 'Мужчин и женщин | Men & women'),
    ]

    SEX_HOUSE = [
        ('1', 'Женщины | Females'),
        ('2', 'Мужчины | Males'),
        ('3', 'Мужчины и женщины | Men & women'),
        ('4', 'Никто не живет | No one lives'),
    ]

    HOUSE_TYPES = [
        ('1', 'Квартира | Apartment'),
        ('2', 'Дом | House'),
        ('3', 'Комната | Room'),
    ]

    HEATINGS = [
        ('1', 'Центральное | Central heating'),
        ('2', 'Электрическое | Electric'),
        ('3', 'Газовое | Gas'),
        ('4', 'Кондиционер | Conditioner'),
        ('5', 'Печное | Stove heating'),
        ('6', 'Отсутствует | No hiating'),
        ('7', 'Другое | Other'),
    ]

    ROOMS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4+'),
        ('5', 'Студия | Studio'),
    ]

    INTERNET = [
        ('1', 'Ethernet/ GPON(optic)'),
        ('2', 'ADSL'),
        ('3', 'Отсутствует | No internet'),
    ]

    INTERIOR = [
        ('1', 'Новый ремонт | Good interior condition'),
        ('2', 'Без ремонта | Old interior'),
        ('3', 'Требуется ремонт | Repair required'),
    ]

    FURNITURE = [
        ('1', 'Полностью | Fully furnished'),
        ('2', 'Частично | Partially furnished'),
        ('3', 'Без мебели | Without furniture'),
    ]

    APPLIANCES = [
        ('1', 'Все необходимое | Necessary'),
        ('2', 'Частично | Partially available'),
        ('3', 'Отсутствует | No appliances'),
        ('4', 'Необходимое и дополнительно | Necessary+'),
    ]

    name = models.CharField(max_length=100, null=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    desired_lodgers_gender = models.CharField(max_length=2, choices=SEX)
    sex_of_now_lodgers = models.CharField(max_length=2, choices=SEX_HOUSE)
    with_kids = models.BooleanField()
    district = models.CharField(max_length=50, null=True, blank=True)
    house_type = models.CharField(max_length=2, choices=HOUSE_TYPES)
    number_of_rooms = models.CharField(max_length=2, choices=ROOMS)
    house_area = models.FloatField(max_length=7)
    interior_condition = models.CharField(max_length=2, choices=INTERIOR)
    furniture = models.CharField(max_length=2, choices=FURNITURE)
    appliances = models.CharField(max_length=2, choices=APPLIANCES)
    heating = models.CharField(max_length=2, choices=HEATINGS)
    internet = models.CharField(max_length=2, choices=INTERNET)
    number_of_lodgers = models.PositiveSmallIntegerField()
    free_space_for_num_person = models.PositiveSmallIntegerField()
    total_cost = models.PositiveSmallIntegerField()
    cost_per_person = models.PositiveSmallIntegerField()
    average_utility_bill = models.PositiveSmallIntegerField(null=True, blank=True)
    min_rental_period = models.PositiveSmallIntegerField()
    separate_room = models.BooleanField()
    has_balcony = models.BooleanField()
    has_loggia = models.BooleanField()
    has_parking = models.BooleanField()
    transport_nearby = models.BooleanField()
    with_animals = models.BooleanField()
    can_smoke = models.BooleanField()
    contacts = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    count_of_views = models.PositiveIntegerField(default=0)
    in_favorites = models.PositiveSmallIntegerField(default=0)
    photo_1 = models.ImageField(upload_to='photos/house_offers', blank=True)
    photo_2 = models.ImageField(upload_to='photos/house_offers', blank=True)
    photo_3 = models.ImageField(upload_to='photos/house_offers', blank=True)
    photo_4 = models.ImageField(upload_to='photos/house_offers', blank=True)

    def __str__(self):
        return str(self.name)

    def get_url(self):
        return reverse('housing_details', args=[self.pk])


