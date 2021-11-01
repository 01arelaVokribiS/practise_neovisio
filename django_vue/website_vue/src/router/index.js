import { createRouter, createWebHistory } from 'vue-router'
import store from '../store' 

import Home from '../views/Home.vue'
import Course from '../views/Course.vue'
import Category from '../views/Category.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/:category_slug/:course_slug',
    name: 'Course',
    component: Course
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        next({
            name: 'LogIn',
            query: {
                to: to.path
            }
        });
    } else {
        next()
    }
})

export default router
