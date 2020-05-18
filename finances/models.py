from django.db import models
from django.contrib.auth.models import User


class BaseFinance(models.Model):
	product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Товар')
	optional_info = models.CharField('Дополнительная информация', max_length=120, blank=True)
	price = models.IntegerField('Стоимость')
	BOOL_CHOICES = ((True, 'Доход'), (False, 'Расход'))
	operation = models.BooleanField('Операция', choices=BOOL_CHOICES, default=True)
	date_added = models.DateTimeField('Дата', auto_now=True)

	@staticmethod
	def all_finances():
		return BaseFinance.objects.all()

	@staticmethod
	def total_money():
		total = 0
		for oper in BaseFinance.objects.all():
			if oper.operation:
				total += oper.price
			else:
				total -= oper.price
		return total

	class Meta:
		verbose_name = "Финанс"
		verbose_name_plural = "Финансы"
		ordering = ['-date_added']

	def __str__(self):

		return '{} {} {}'.format(self.product, self.optional_info, self.operation)


class Product(models.Model):

	name = models.CharField('Название',max_length=50)
	quantity = models.IntegerField('Количество', blank=True, null=True)
	price = models.IntegerField('Цена')
	image = models.ImageField('Изображение', upload_to='images/products')
	description = models.CharField('Описание', max_length=120, blank=True)
	category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, related_name='product')
	date_added = models.DateTimeField(auto_now=True)
	available = models.BooleanField('Наличие', default=True)

	def check_av(self):
		if self.quantity < 1:
			self.available = False

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.name


class ProductMixin:

	def check_available(self, q):
		if q < 1:
			self.available = False


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

	product = models.ForeignKey(Product, related_name='product', verbose_name='Товар', on_delete=models.PROTECT)
	available = models.BooleanField('Наличие', default=True)

	class Meta:
		verbose_name = 'Размеры'
		verbose_name_plural = 'Размеры'


class OuterwearDetail(ProductDetail):
	size = models.ForeignKey(Size, related_name='size', verbose_name='Размер', on_delete=models.PROTECT)
	quantity_size = models.IntegerField('Количество')

	@staticmethod
	def total_quantity(pr_id):
		return sum([i.quantity_size for i in (val for val in OuterwearDetail.objects.filter(product=pr_id))])

	@staticmethod
	def all_sizes():
		size_quantity = []
		for product in Product.objects.all():
			d = dict()
			for product_size in OuterwearDetail.objects.filter(product=product):
				d[product_size.size.name] = product_size.available
			size_quantity.append({product.pk: d})
		return size_quantity

	@staticmethod
	def all_outer():
		size_quantity = []
		for product in Product.objects.all():
			d = dict()
			for product_size in OuterwearDetail.objects.filter(product=product):
				d[product_size.size.name] = product_size.quantity_size
			if len(d) > 0:
				size_quantity.append({product.name: d})
		return size_quantity

	def __str__(self):
		return '{} {}'.format(self.product.name, self.size)

	class Meta:
		verbose_name = 'Верхняя Одежда'
		verbose_name_plural = 'Верхняя Одежда'


class OtherDetail(ProductDetail):

	def other_quantity(self):
		return Product.objects.filter(pk=self.product.pk).first().quantity

	def __str__(self):
		return self.product.name

	class Meta:
		verbose_name = 'Другой товар'
		verbose_name_plural = 'Другие товары'


class Debt(models.Model):
	value = models.IntegerField('Сумма')
	description = models.CharField('Описание', max_length=120)
	user = models.ForeignKey(User, verbose_name='Участник', on_delete=models.PROTECT, related_name='debts')

	class Meta:
		verbose_name = 'Долг'
		verbose_name_plural = 'Долги'

	def __str__(self):
		if self.user.first_name:
			name = self.user.first_name
		else:
			name = self.user.username
		return '{}: {} {}'.format(name, self.description, self.value)
