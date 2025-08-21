from django import forms
class FormOrder(forms.Form):
    name = forms.CharField(label='имя', max_length=30)
    f_name = forms.CharField(label='фамилия', max_length=30)
    email = forms.EmailField()
    product = forms.ChoiceField(choices=((1,'5 л'), (2,'10л'),(3,'15л'))) 