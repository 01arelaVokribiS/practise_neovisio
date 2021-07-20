from .models import Client, Employee, Course
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), empty_label='Select Client')
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label='Select Employee')
    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label='Select Course')

    class Meta:
        model = Order
        fields = ['client', 'employee', 'course'] # what fields will be displayed in form
