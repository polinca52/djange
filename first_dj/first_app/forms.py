from django import forms
class Registr(forms.Form):
    name = forms.CharField(label='имя', max_length=30)
    f_name = forms.CharField(label='фамилия', max_length=30)