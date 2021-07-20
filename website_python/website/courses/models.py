from django.db import models
from categories.models import Category

# table courses
class Course(models.Model):
    name = models.CharField('Name', max_length=70, db_index=True)
    description = models.TextField('Description')
    price = models.DecimalField('Price', max_digits=7, decimal_places=2, help_text='Please enter price less than 10 000.00') # max_digits=7 and decimal_places=2 equals <10 000.00
    available = models.BooleanField('Available', default=True)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE) # foreign key category

    class Meta:
        ordering = ('name',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        
    # override display method. Output course name
    def __str__(self):
        return self.name