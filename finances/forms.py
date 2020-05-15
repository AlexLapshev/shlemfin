from django import forms
from .models import Outerwear


class OuterwearForm(forms.ModelForm):
	CHOICES = (("", "---------"), ('s', 'S',), ('m', 'M',), ('l', 'L',), ('xl', 'XL',), ('xxl', 'XXL',))
	size = forms.ChoiceField(choices=CHOICES, label='Размер', required=True)
	optional_info = forms.CharField(max_length=120, label='Дополнительно', required=False)

	class Meta:
		model = Outerwear
		fields = ['price']
		labels = {
			'price': "Цена",
		}

# class BaseFinanceForm(forms.ModelForm):
# 	class Meta:
# 		exclude = []
#
#
# class ExampleModelForm(BaseFinanceForm):
# 	class Meta(BaseFinanceForm.Meta):
# 		model = BaseFinance


# class SizeForm(forms.Form):
# 	CHOICES = (("False", "---------"), ('s', 'S',), ('m', 'M',), ('l', 'L',), ('xl', 'XL',), ('xxl', 'XXL',))
# 	size = forms.ChoiceField(choices=CHOICES, )
#
#
# class BaseFinanceForm(forms.ModelForm):
# 	class Meta:
# 		model = BaseFinance
# 		fields = ['product', 'value', 'operation', 'title']


