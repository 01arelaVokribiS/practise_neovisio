from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Order
from .forms import OrderForm

# orders index page
class OrderIndexView(ListView):
    paginate_by = 5 # number of records to display in table
    model = Order
    template_name = 'orders/index.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Orders'
        return context

    def get_queryset(self):
        return Order.objects.all()

# create order
class OrderCreateView(CreateView):
    model = Order
    template_name = 'orders/create.html'
    success_url = reverse_lazy('orders:index')
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Order'
        return context

# update order data
class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'orders/create.html'
    success_url = reverse_lazy('orders:index')
    form_class = OrderForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Order'
        return context

# delete order
class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:index')
    template_name = 'orders/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Order'
        return context
