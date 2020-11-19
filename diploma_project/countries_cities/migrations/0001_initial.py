# Generated by Django 3.1.3 on 2020-11-19 19:09

import countries_cities.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название Страны')),
                ('description', models.TextField(verbose_name='Описание Страны')),
                ('slug', models.SlugField(max_length=150, verbose_name='Ссылка')),
                ('icon', models.ImageField(upload_to=countries_cities.models.Country.load_photo, verbose_name='Флаг Страны')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название Страны')),
                ('foundation_date', models.IntegerField(verbose_name='Год основания')),
                ('population', models.IntegerField(verbose_name='Население')),
                ('description', models.TextField(verbose_name='Описание Города')),
                ('image', models.ImageField(upload_to=countries_cities.models.City.load_photo, verbose_name='Фото Города')),
                ('slug', models.SlugField(max_length=150, verbose_name='Ссылка')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='countries_cities.country', verbose_name='Название страны')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'db_table': 'city',
            },
        ),
    ]
