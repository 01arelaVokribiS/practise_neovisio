from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeIndexView.as_view(), name='index'),                  # url to index page
    path('create', views.EmployeeCreateView.as_view(), name='create'),          # url to create page
    path('<int:pk>/update', views.EmployeeUpdateView.as_view(), name='update'), # url to update page
    path('<int:pk>/delete', views.EmployeeDeleteView.as_view(), name='delete'), # url to delete page
]