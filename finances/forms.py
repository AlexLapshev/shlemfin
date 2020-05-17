from django import forms
from .models import BaseFinance, Size


class BaseFinanceForm(forms.ModelForm):
	CHOICES = [('', '---------')] + [(str(i.name), i.name) for i in Size.objects.all()]
	size = forms.ChoiceField(choices=CHOICES, label='Размер', required=False)

	class Meta:
		model = BaseFinance
		fields = '__all__'


#
#
# class OuterwearForm(forms.ModelForm):
# 	CHOICES = (("", "---------"), ('s', 'S',), ('m', 'M',), ('l', 'L',), ('xl', 'XL',), ('xxl', 'XXL',))
# 	size = forms.ChoiceField(choices=CHOICES, label='Размер', required=True)
# 	optional_info = forms.CharField(max_length=120, label='Дополнительно', required=False)
#
# 	class Meta:
# 		model = Outerwear
# 		fields = ['price']
# 		labels = {
# 			'price': "Цена",
# 		}
#
#
# class OtherForm(forms.ModelForm):
# 	optional_info = forms.CharField(max_length=120, label='Дополнительно', required=False)
#
# 	class Meta(OuterwearForm.Meta):
# 		model = Other
#
#
# class DebtForm(forms.ModelForm):
#
# 	class Meta:
# 		model = Debt
# 		fields = ['value', 'description', 'user']
#
#
