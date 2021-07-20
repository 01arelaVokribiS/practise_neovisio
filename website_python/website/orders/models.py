from django.db import models
from django.urls import reverse
from clients.models import Client
from courses.models import Course
from employees.models import Employee

# table orders
class Order(models.Model):
    client = models.ForeignKey(Client, related_name='clients', on_delete=models.CASCADE) # foreign key client
    employee = models.ForeignKey(Employee, related_name='employees', on_delete=models.CASCADE) # foreign key employee
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.CASCADE) # foreign key course

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
