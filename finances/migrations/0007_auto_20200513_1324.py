# Generated by Django 3.0.6 on 2020-05-13 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0006_auto_20200513_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tape',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finances.Product')),
            ],
            options={
                'verbose_name': 'Кассета',
                'verbose_name_plural': 'Кассеты',
            },
            bases=('finances.product',),
        ),
        migrations.AddField(
            model_name='basefinance',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finances.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=1, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basefinance',
            name='title',
            field=models.CharField(blank=True, max_length=120, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Longsleeve',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='finances.Product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.Size', verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Лонгслив',
                'verbose_name_plural': 'Лонгсливы',
            },
            bases=('finances.product',),
        ),
    ]