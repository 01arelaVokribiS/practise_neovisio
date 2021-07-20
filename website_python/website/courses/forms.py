from categories.models import Category
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    available = forms.BooleanField(required=False, initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Select Category')

    class Meta:
        model = Course
        fields = ['name', 'description', 'price', 'available', 'category'] # what fields will be displayed in form
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            'description': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'price': forms.NumberInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter price'
            })
        }
