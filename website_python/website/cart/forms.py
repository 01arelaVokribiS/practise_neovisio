from django import forms

# form to add item in cart
class CartAddCourseForm(forms.Form):
    quantity = forms.IntegerField(label='', widget=forms.NumberInput(attrs={
        'min': '1',
        'max': '25',
        'class': 'form-control',
        'placeholder': 'Input quantity'
    }))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
