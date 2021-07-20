from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.CategoryIndexView.as_view(), name='index'),                  # url to index page
    path('create', views.CategoryCreateView.as_view(), name='create'),          # url to create page
    path('<int:pk>/update', views.CategoryUpdateView.as_view(), name='update'), # url to update page
    path('<int:pk>/delete', views.CategoryDeleteView.as_view(), name='delete')  # url to delete page
]