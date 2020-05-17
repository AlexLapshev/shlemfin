from django.db import models
from django.contrib.auth.models import User


class BaseFinance(models.Model):
	product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Товар')
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
	name = models.CharField('Название',max_length=50)
	quantity = models.IntegerField('Количество', blank=True, null=True)
	price = models.IntegerField('Цена')
	image = models.ImageField('Изображение', upload_to='images/products')
	description = models.CharField('Описание', max_length=120, blank=True)

	category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, related_name='product')
	date_added = models.DateTimeField(auto_now=True)
	available = models.BooleanField('Наличие', default=True)

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.name


class ProductMixin:

	def check_available(self):
		if self.quantity < 1:
			self.available = False
		else:
			self.available = True


class Category(models.Model):
	name = models.CharField('Категория', max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Size(models.Model):
	name = models.CharField('Размер', max_length=4)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Размер'
		verbose_name_plural = 'Размеры'


class ProductDetail(models.Model, ProductMixin):

	product = models.ForeignKey(Product, related_name='product_size', verbose_name='Товар', on_delete=models.PROTECT)
	quantity = models.IntegerField('Количество')
	available = models.BooleanField('Наличие', default=True)

	class Meta:
		verbose_name = 'Размеры'
		verbose_name_plural = 'Размеры'


class OuterwearDetail(ProductDetail):
	size = models.ForeignKey(Size, related_name='size', verbose_name='Размер', on_delete=models.PROTECT)

	def __str__(self):
		return '{} {}'.format(self.product.name, self.size)

	class Meta:
		verbose_name = 'Размер'
		verbose_name_plural = 'Размеры'


class Debt(models.Model):
	value = models.IntegerField('Сумма')
	description = models.CharField('Описание', max_length=120)
	user = models.ForeignKey(User, verbose_name='Участник', on_delete=models.PROTECT, related_name='debts')

	class Meta:
		verbose_name = 'Долг'
		verbose_name_plural = 'Долги'

	def __str__(self):
		return '{}: {}'.format(self.user.first_name, self.value)
