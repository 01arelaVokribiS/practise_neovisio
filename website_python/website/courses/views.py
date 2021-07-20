from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Course
from .forms import CourseForm

# courses index page
class CourseIndexView(ListView):
    paginate_by = 5 # number of records to display in table
    model = Course
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Courses'
        return context

    def get_queryset(self):
        return Course.objects.all()

# create course
class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/create.html'
    success_url = reverse_lazy('courses:index')
    form_class = CourseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Course'
        return context

# update course data
class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/create.html'
    success_url = reverse_lazy('courses:index')
    form_class = CourseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Course'
        return context

# delete course
class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:index')
    template_name = 'courses/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Course'
        return context
