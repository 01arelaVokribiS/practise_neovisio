from django.forms import ModelForm, TextInput
from .models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug'] # what fields will be displayed in form
        widgets = {
            'name': TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            'slug': TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter slug'
            })
        }