from django import forms

# CREATE A form
class input_form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
