from django.db import models
from django.urls import reverse

# table employees
class Employee(models.Model):
    surname = models.CharField('Surname', max_length=70, db_index=True)
    name = models.CharField('Name', max_length=70)
    middlename = models.CharField('Middlename', max_length=70, blank=True)
    position = models.CharField('Position', max_length=70)

    class Meta:
        ordering = ['id', 'surname']
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    # override display method. Output employee's surname
    def __str__(self):
        return self.surname