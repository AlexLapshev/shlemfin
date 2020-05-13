# Generated by Django 3.0.6 on 2020-05-13 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finances', '0010_auto_20200513_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basefinance',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='finances', to='finances.Product', verbose_name='Товар'),
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Сумма')),
                ('description', models.CharField(max_length=120, verbose_name='Описание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='debts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]