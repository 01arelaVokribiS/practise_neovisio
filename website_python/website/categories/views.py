from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm

# categories index page
class CategoryIndexView(ListView):
    paginate_by = 5 # number of records to display in table
    model = Category
    template_name = 'categories/index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categories'
        return context

    def get_queryset(self):
        return Category.objects.all()

# create category
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/create.html'
    success_url = reverse_lazy('categories:index')
    form_class = CategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Category'
        return context

# update category data
class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'categories/create.html'
    success_url = reverse_lazy('categories:index')
    form_class = CategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Category'
        return context

# delete category
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories:index')
    template_name = 'categories/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Category'
        return context
