__author__ = 'Javier'


from django import forms

class RepositoryRequestForm(forms.Form):
    user = forms.CharField(max_length=100)
    repository_name = forms.CharField()