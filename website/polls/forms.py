from django import forms


class email_form(forms.Form):
    email = forms.EmailField(max_length=32, label="Gmail")
