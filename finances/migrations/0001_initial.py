# Generated by Django 3.0.6 on 2020-05-15 05:32

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
            name='BaseFinance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optional_info', models.CharField(blank=True, max_length=120, verbose_name='Дополнительная информация')),
                ('price', models.IntegerField(verbose_name='Рубли')),
                ('operation', models.BooleanField(choices=[(True, 'Доход'), (False, 'Расход')], default=True, verbose_name='Операция')),
                ('date_added', models.DateTimeField(auto_now=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Финанс',
                'verbose_name_plural': 'Финансы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Наименование')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='images/products', verbose_name='Изображение')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finances.Product')),
            ],
            options={
                'verbose_name': 'Другой Товар',
                'verbose_name_plural': 'Другие Товары',
            },
            bases=('finances.product',),
        ),
        migrations.CreateModel(
            name='Outerwear',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finances.Product')),
                ('s', models.IntegerField(verbose_name='S')),
                ('m', models.IntegerField(verbose_name='M')),
                ('l', models.IntegerField(verbose_name='L')),
                ('xl', models.IntegerField(verbose_name='XL')),
                ('xxl', models.IntegerField(verbose_name='XXL')),
            ],
            options={
                'verbose_name': 'Верхняя одежда',
                'verbose_name_plural': 'Верхняя одежда',
            },
            bases=('finances.product', models.Model),
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Сумма')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='debts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Долг',
                'verbose_name_plural': 'Долги',
            },
        ),
    ]
