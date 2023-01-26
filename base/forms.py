from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S','Stripe'),
    ('P','Paypal')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput())
    apartement_address = forms.CharField(required=False)
    country = CountryField(blank_label="(select country)").formfield(
        widget = CountrySelectWidget(attrs={
            'class' : 'custem-select d-block w-100',
        })
    )
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'zip'
    }))
    same_shipping_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())

    payement_option = forms.ChoiceField(widget=forms.RadioSelect(),choices=PAYMENT_CHOICES)
