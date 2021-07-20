from django.urls.base import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from .models import Employee
from .forms import EmployeeForm

# clients index page
class EmployeeIndexView(ListView):
    paginate_by = 5 # number of records to display in table
    model = Employee
    template_name = 'employees/index.html'
    context_object_name = 'employees'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Employees'
        return context

    def get_queryset(self):
        return Employee.objects.all()

# create client
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employees/create.html'
    success_url = reverse_lazy('employees:index')
    form_class = EmployeeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Employee'
        return context

# update client data
class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employees/create.html'
    success_url = reverse_lazy('employees:index')
    form_class = EmployeeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Employee'
        return context

# delete client 
class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees:index')
    template_name = 'employees/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Employee'
        return context
