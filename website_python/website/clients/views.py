from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm

# clients index page
class ClientIndexView(ListView):
    paginate_by = 5 # number of records to display in table
    model = Client
    template_name = 'clients/index.html'
    context_object_name = 'clients'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Clients'
        return context

    def get_queryset(self):
        return Client.objects.all()

# create client
class ClientCreateView(CreateView):
    model = Client
    template_name = 'clients/create.html'
    success_url = reverse_lazy('clients:index')
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Client'
        return context

# update client data
class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'clients/create.html'
    success_url = reverse_lazy('clients:index')
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Client'
        return context

# delete client 
class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:index')
    template_name = 'clients/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Client'
        return context
