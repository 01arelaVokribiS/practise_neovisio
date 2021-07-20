from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),                        # url cart main page
    path('add/<int:course_id>/', views.cart_add, name='cart_add'),          # url add item in cart
    path('remove/<int:course_id>/', views.cart_remove, name='cart_remove'), # url delete item from cart
]