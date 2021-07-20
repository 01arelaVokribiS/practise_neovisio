from cart.forms import CartAddCourseForm
from django.shortcuts import render
from django.views.generic.detail import DetailView
from courses.models import Course

# main page
def index(request):
    courses = Course.objects.all()[:4]
    context = {
        'title': 'Main', # header page title
        'courses': courses,
    }

    return render(request, 'main/home/index.html', context)

# display data detail
class CourseDetailView(DetailView):
    model = Course
    template_name = 'main/home/details_view.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course Detail'
        return context

def about(request):
    context = {
        'title': 'About', # header page title
    }

    return render(request, 'main/home/about.html', context)

def all_courses(request):
    courses = Course.objects.all()
    cart_product_form = CartAddCourseForm()
    context = {
        'title': 'Courses', # header page title
        'courses': courses,
        'cart_product_form': cart_product_form
    }

    return render(request, 'main/home/courses.html', context)