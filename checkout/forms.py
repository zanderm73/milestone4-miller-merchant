from django import forms
from .models import Order

# payment form, specific fields are required by stripe for transaction to be successful
class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    billing_address = forms.CharField(label='Registered Card Address', required=False)
    street_postcode = forms.CharField(label='Registered Card Postcode', required=False)

# form to gather delivery information from the user
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number','delivery_address', 'city',
            'postcode', 'country'
        )