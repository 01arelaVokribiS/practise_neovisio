from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *

from ..models import *


class CoursesList(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)


class CourseDetail(APIView):
    def get_object(self, category_slug, course_slug):
        try:
            return Course.objects.filter(category__slug=category_slug).get(slug=course_slug)
        except Course.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, course_slug, format=None):
        course = self.get_object(category_slug, course_slug)
        serializer = CourseSerializer(course)

        return Response(serializer.data)


class CategoriesList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)

        return Response(serializer.data)