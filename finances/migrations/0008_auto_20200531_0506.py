# Generated by Django 3.0.6 on 2020-05-31 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0007_auto_20200531_0319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendto',
            options={'verbose_name': 'Куда Отправлять', 'verbose_name_plural': 'Куда Отправлять'},
        ),
        migrations.AlterField(
            model_name='sendto',
            name='send_description',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Дополнительная Информация'),
        ),
    ]