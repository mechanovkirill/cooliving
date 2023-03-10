# Generated by Django 4.1.4 on 2023-01-03 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=256, unique=True)),
                ('district', models.CharField(blank=True, max_length=50, null=True)),
                ('gender_of_living', models.PositiveSmallIntegerField(choices=[(1, 'Женщины | Females'), (2, 'Мужчины | Males'), (3, 'Смешанно | Mixed')])),
                ('desired_gender', models.PositiveSmallIntegerField(choices=[(1, 'Женщины | Females'), (2, 'Мужчины | Males'), (3, 'Смешанно | Mixed')])),
                ('house_type', models.PositiveSmallIntegerField(choices=[(1, 'Квартира | Apartment'), (2, 'Дом | House'), (3, 'Комната | Room')])),
                ('number_of_rooms', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5+')])),
                ('heating', models.PositiveSmallIntegerField(choices=[(1, 'Центральное | Central heating'), (2, 'Электрическое | '), (3, 'Собственный газовый котел | '), (4, 'Кондиционер | '), (6, 'Печное | '), (5, 'Отсутствует | '), (7, 'Другое | ')])),
                ('internet', models.PositiveSmallIntegerField(choices=[(1, 'Кабельный | '), (2, 'ADSL'), (3, 'Отсутствует | ')])),
                ('interior_condition', models.PositiveSmallIntegerField(choices=[(1, 'Новый ремонт | '), (2, 'Без ремонта | ')])),
                ('furniture', models.PositiveSmallIntegerField(choices=[(1, 'Полностью | '), (2, 'Частично | '), (3, 'Без мебели | ')])),
                ('count_of_living', models.PositiveSmallIntegerField()),
                ('wanted_quantity_of_person', models.PositiveSmallIntegerField()),
                ('total_cost', models.FloatField(max_length=10)),
                ('cost_per_person', models.FloatField(max_length=10)),
                ('rental_period', models.PositiveSmallIntegerField()),
                ('with_animals', models.BooleanField(default=False)),
                ('contacts', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=512)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(blank=True, max_length=254, null=True, upload_to='photos/house_offers')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OfferGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(max_length=254, upload_to='photos/house_offers')),
                ('offer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='offers.offer')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.countries'),
        ),
    ]
