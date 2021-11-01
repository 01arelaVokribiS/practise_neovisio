from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    slug = models.SlugField(verbose_name='Slug', max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Course(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100)
    slug = models.SlugField(verbose_name='Slug', max_length=100, unique=True)
    image = models.ImageField(verbose_name='Image', upload_to='uploads/', blank=True, null=True)
    description = models.TextField(verbose_name='Description', null=True)
    price = models.DecimalField(verbose_name='Price', max_digits=6, decimal_places=2)
    available = models.BooleanField(verbose_name='Available', default=True)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''