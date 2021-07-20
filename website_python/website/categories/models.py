from django.db import models
from django.urls import reverse

# table categories
class Category(models.Model):
    name = models.CharField('Name', max_length=100)
    slug = models.CharField('Slug', max_length=100, unique=True)

    class Meta:
        ordering = ['name',]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # override display method. Output category name
    def __str__(self):
        return self.name