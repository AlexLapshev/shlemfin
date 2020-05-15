from django.db import models
from django.contrib.auth.models import User
from model_utils.managers import InheritanceManager


class BaseFinance(models.Model):
	optional_info = models.CharField('Дополнительная информация', max_length=120, blank=True)
	price = models.IntegerField('Рубли')
	BOOL_CHOICES = ((True, 'Доход'), (False, 'Расход'))
	operation = models.BooleanField('Операция', choices=BOOL_CHOICES, default=True)
	date_added = models.DateTimeField('Дата', auto_now=True)

	class Meta:
		verbose_name = "Финанс"
		verbose_name_plural = "Финансы"
		ordering = ['-date_added']

	def __str__(self):
		return self.optional_info


class Product(models.Model):
	name = models.CharField('Наименование', max_length=120)
	price = models.IntegerField('Цена')
	image = models.ImageField('Изображение', upload_to='images/products')
	quantity = models.IntegerField('Количество', blank=True, null=True)
	available = models.BooleanField('Наличие', default=True)

	objects = InheritanceManager()

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	# abstract = True

	def __str__(self):
		return self.name


class Other(Product):
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Другой Товар'
		verbose_name_plural = 'Другие Товары'


class SizeMixin(models.Model):
	s = models.IntegerField('S')
	m = models.IntegerField('M')
	l = models.IntegerField('L')
	xl = models.IntegerField('XL')
	xxl = models.IntegerField('XXL')

	def total_quantity(self):
		return sum[self.s, self.m, self.l, self.xl, self.xxl]

	class Meta:
		abstract = True


class Outerwear(Product, SizeMixin):

	@classmethod
	def all_outer_wear(cls):
		all_outer = []
		for i in cls.objects.all():
			all_outer.append({
				'name': i.name,
				'img': i.image.url,
				'sizes': {
					's': i.s,
					'm': i.m,
					'l': i.l,
					'xl': i.xl,
					'xxl': i.xxl,
				},
				'id': i.id,
				'price': i.price
			})
		return all_outer

	class Meta:
		verbose_name = 'Верхняя одежда'
		verbose_name_plural = 'Верхняя одежда'

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
