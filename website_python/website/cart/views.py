from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from courses.models import Course
from .cart import Cart
from .forms import CartAddCourseForm


@require_POST
# add item in cart
def cart_add(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Course, id=course_id)
    form = CartAddCourseForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(course=course,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

# delete item from cart
def cart_remove(request, course_id):
    cart = Cart(request)
    course = get_object_or_404(Course, id=course_id)
    cart.remove(course)
    return redirect('cart:cart_detail')

# display in form item quantity and update button
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddCourseForm(initial = {
                'quantity': item['quantity'],
                'update': True
            })
    
    context = {
        'title': 'Cart',
        'cart': cart
    }
    return render(request, 'cart/detail.html', context)