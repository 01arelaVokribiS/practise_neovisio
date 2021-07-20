from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),                                # url to main page of website
    path('<int:pk>/detail', views.CourseDetailView.as_view(), name='detail'), # url to course  details
    path('about', views.about, name='about'), # url to course  details
    path('courses', views.all_courses, name='courses'), # url to course  details
]