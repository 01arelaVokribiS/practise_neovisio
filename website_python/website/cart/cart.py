from decimal import Decimal
from django.conf import settings
from courses.models import Course

class Cart(object):
    def __init__(self, request):
        """
        Cart initilization
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        # save empty cart in session
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
            Iterating items in cart and get items from database
        """
        course_ids = self.cart.keys()
        # get items and add it in cart
        courses = Course.objects.filter(id__in=course_ids)

        cart = self.cart.copy()
        for course in courses:
            cart[str(course.id)]['course'] = course

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
            Count how many items in cart
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, course, quantity=1, update_quantity=False):
        """
            Add item in cart or updating its quantity
        """
        course_id = str(course.id)
        if course_id not in self.cart:
            self.cart[course_id] = { 'quantity': 0,
                                     'price': str(course.price) }
        if update_quantity:
            self.cart[course_id]['quantity'] = quantity
        else:
            self.cart[course_id]['quantity'] += quantity
        self.save()

    # save cart item
    def save(self):
        self.session.modified = True

    def remove(self, course):
        """
            Deleting cart item
        """
        course_id = str(course.id)
        if course_id in self.cart:
            del self.cart[course_id]
            self.save()
    
    # get total price
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    # clear cart in session
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
