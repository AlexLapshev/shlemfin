from django.db import models
from django.contrib.auth.models import User


class BaseFinance(models.Model):
	product = models.ForeignKey('Product', verbose_name='Товар', on_delete=models.PROTECT, null=True, blank=True, related_name='finances')
	value = models.IntegerField('Рубли')
	title = models.CharField('Название', max_length=120, blank=True)
	date_added = models.DateTimeField('Дата', auto_now=True)
	BOOL_CHOICES = ((True, 'Доход'), (False, 'Расход'))

	operation = models.BooleanField('Операция', choices=BOOL_CHOICES)

	class Meta:
		verbose_name = "Финанс"
		verbose_name_plural = "Финансы"

	def __str__(self):
		if self.product:
			return self.product.name
		else:
			return self.title


class Product(models.Model):
	name = models.CharField('Наименование', max_length=120)
	price = models.IntegerField('Цена')
	quantity = models.IntegerField('Количество')

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товар'

	def __str__(self):
		return self.name


class Size(models.Model):

	size = models.CharField('Размер', max_length=3)

	class Meta:
		verbose_name = 'Размер'
		verbose_name_plural = 'Размеры'

	def __str__(self):
		return self.size


class Tshirt(Product):
	size = models.ForeignKey('Size', verbose_name='Размер', on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Футболка'
		verbose_name_plural = 'Футболки'

	def __str__(self):
		return self.name


class Longsleeve(Product):
	size = models.ForeignKey('Size', verbose_name='Размер', on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Лонгслив'
		verbose_name_plural = 'Лонгсливы'

	def __str__(self):
		return self.name


class Tape(Product):
	pass

	class Meta:
		verbose_name = 'Кассета'
		verbose_name_plural = 'Кассеты'

	def __str__(self):
		return self.name


class Debt(models.Model):
	value = models.IntegerField('Сумма')
	description = models.CharField('Описание', max_length=120)
	user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='debts')

	class Meta:
		verbose_name = 'Долг'
		verbose_name_plural = 'Долги'

	def __str__(self):
		return '{}: {}'.format(self.user.first_name, self.value)