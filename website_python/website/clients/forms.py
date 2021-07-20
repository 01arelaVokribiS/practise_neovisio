from django.forms import ModelForm, TextInput
from .models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['surname', 'name', 'middlename', 'birth_date', 'telephone_number', 'address'] # what fields will be displayed in form
        widgets = {
            'surname': TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter surname'
            }),
            'name': TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            'middlename': TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter middlename'
            }),
            'birth_date': TextInput(attrs = {
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Enter birthday date'
            }),
            'telephone_number': TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter telephone number'
            }),
            'address': TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter address'
            })
        }
