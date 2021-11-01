from django.urls import path

from . import api_views


urlpatterns = [
    path('courses/', api_views.CoursesList.as_view()),
    path('categories/', api_views.CategoriesList.as_view()),
    path('courses/<slug:category_slug>/<slug:course_slug>/', api_views.CourseDetail.as_view()),
    path('courses/<slug:category_slug>/', api_views.CategoryDetail.as_view())
]
