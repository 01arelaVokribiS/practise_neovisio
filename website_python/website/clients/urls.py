from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.ClientIndexView.as_view(), name='index'),                  # url to index page
    path('create', views.ClientCreateView.as_view(), name='create'),          # url to create page
    path('<int:pk>/update', views.ClientUpdateView.as_view(), name='update'), # url to update page
    path('<int:pk>/delete', views.ClientDeleteView.as_view(), name='delete'), # url to delete page
]