# Generated by Django 3.0.6 on 2020-05-17 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import finances.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество')),
                ('image', models.ImageField(upload_to='images/products', verbose_name='Изображение')),
                ('description', models.CharField(blank=True, max_length=120, verbose_name='Описание')),
                ('category', models.CharField(max_length=120, verbose_name='Категория')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_size', to='finances.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Размеры',
                'verbose_name_plural': 'Размеры',
            },
            bases=(models.Model, finances.models.ProductMixin),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4, verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Сумма')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='debts', to=settings.AUTH_USER_MODEL, verbose_name='Участник')),
            ],
            options={
                'verbose_name': 'Долг',
                'verbose_name_plural': 'Долги',
            },
        ),
        migrations.CreateModel(
            name='BaseFinance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optional_info', models.CharField(blank=True, max_length=120, verbose_name='Дополнительная информация')),
                ('price', models.IntegerField(verbose_name='Рубли')),
                ('operation', models.BooleanField(choices=[(True, 'Доход'), (False, 'Расход')], default=True, verbose_name='Операция')),
                ('date_added', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finances.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Финанс',
                'verbose_name_plural': 'Финансы',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='OuterwearDetail',
            fields=[
                ('productdetail_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finances.ProductDetail')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='size', to='finances.Size', verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
            },
            bases=('finances.productdetail',),
        ),
    ]
