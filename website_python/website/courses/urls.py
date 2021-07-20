from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseIndexView.as_view(), name='index'),                  # url to index page
    path('create', views.CourseCreateView.as_view(), name='create'),          # url to create page
    path('<int:pk>/update', views.CourseUpdateView.as_view(), name='update'), # url to update page
    path('<int:pk>/delete', views.CourseDeleteView.as_view(), name='delete')  # url to delete page
]