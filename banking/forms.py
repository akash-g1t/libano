from django import forms
from .models import Banking
from django.core.exceptions import ValidationError

class BankingForm(forms.ModelForm):
    class Meta:
        model = Banking
        fields = ['email', 'url', 'account_number', 'ifsc_code', 'expiry_date', 'amount']

    def clean(self):
        cd = self.cleaned_data
        ifsc_code = cd.get('ifsc_code')
        expiry_date = cd.get('expiry_date')
        if '/' not in expiry_date:
            raise ValidationError('Invalid Expiry Date')
        if not int(expiry_date[:2]) and not int(expiry_date[3:]):
            raise ValidationError('Invalid Expiry Date')

        return cd