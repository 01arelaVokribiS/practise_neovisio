from django.forms import ModelForm, TextInput
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['surname', 'name', 'middlename', 'position'] # what fields will be displayed in form
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
            'position': TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter position'
            })
        }
