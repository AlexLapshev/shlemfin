from django import forms
from .models import Outerwear, Other


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


class OtherForm(forms.ModelForm):
	optional_info = forms.CharField(max_length=120, label='Дополнительно', required=False)

	class Meta(OuterwearForm.Meta):
		model = Other


