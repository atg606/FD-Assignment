from django import forms

class AmountForm(forms.Form):
    amount = forms.DecimalField(max_digits=11, decimal_places=2, min_value=1, max_value=99999999999, label="Amount (Rs)")
