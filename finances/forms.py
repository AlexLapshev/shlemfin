from django import forms
from .models import BaseFinance, Product


class BaseFinanceForm(forms.ModelForm):
	class Meta:
		model = BaseFinance
		fields = ['product', 'value', 'operation', 'title']

