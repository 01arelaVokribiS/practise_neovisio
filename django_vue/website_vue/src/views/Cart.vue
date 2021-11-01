<template>
    <table class="table" v-if="cartTotalLength">
        <thead>
            <tr>
                <th>Course</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Total</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            <CartItem
                v-for="item in cart.items"
                :key="item.course.id"
                :initialItem="item"
                v-on:removeFromCart="removeFromCart"
            />
        </tbody>
    </table>
    <div v-else>No products in cart</div>
    <div>
        <strong>{{ cartTotalPrice.toFixed(2) }}$, {{ cartTotalLength }} items</strong>
        <router-link to="/cart/checkout">Checkout</router-link>
    </div>
</template>

<script>
import axios from 'axios'

import CartItem from '@/components/CartItem.vue'

export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart

        document.title = 'Cart'
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.course.id !== item.course.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, currentValue) => {
                return acc += currentValue.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, currentValue) => {
                return acc += currentValue.course.price * currentValue.quantity
            }, 0)
        }
    }
}
</script>