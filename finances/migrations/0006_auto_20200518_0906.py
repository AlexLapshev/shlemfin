# Generated by Django 3.0.6 on 2020-05-18 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_auto_20200518_0721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outerweardetail',
            old_name='quantity',
            new_name='quantity_size',
        ),
    ]