# Generated by Django 3.0.6 on 2020-05-17 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=30, verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='finances.Category', verbose_name='Категория'),
        ),
    ]
