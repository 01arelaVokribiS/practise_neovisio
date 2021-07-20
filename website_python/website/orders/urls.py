from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.OrderIndexView.as_view(), name='index'),                  # url to index page
    path('create', views.OrderCreateView.as_view(), name='create'),          # url to create page
    path('<int:pk>/update', views.OrderUpdateView.as_view(), name='update'), # url to update page
    path('<int:pk>/delete', views.OrderDeleteView.as_view(), name='delete')  # url to delete page
]