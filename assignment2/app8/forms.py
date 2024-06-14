from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Message")
    date = forms.DateField(label="Date (YYYY-MM-DD)")
