from django.db import models
from django.urls import reverse

# table clients
class Client(models.Model):
    surname = models.CharField('Surname', max_length=70, db_index=True) # db_index=True indexing by field
    name = models.CharField('Name', max_length=30)
    middlename = models.CharField('Middlename', max_length=70, blank=True) # blank=True possible to add empty value
    birth_date = models.DateField('BirthDate')
    telephone_number = models.CharField('Telephone', max_length=13) # corresponds to the value: +375 11 1111111
    address = models.CharField('Address', max_length=100)

    class Meta:
        ordering = ['id', 'surname']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    # override display method. Output client's surname
    def __str__(self):
        return self.surname