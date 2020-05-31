from django import forms
from .models import BaseFinance, Size, SendTo


class BaseFinanceForm(forms.ModelForm):
    CHOICES = [('False', '----')] + [(str(i.name), i.name) for i in Size.objects.all()]
    size = forms.ChoiceField(choices=CHOICES, label='Размер')

    class Meta:
        model = BaseFinance
        fields = '__all__'


class SendToForm(forms.ModelForm):

    class Meta:
        model = SendTo
        fields = ('fcs', 'where', 'send_description')
