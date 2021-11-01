<template>
    <div>
        Checkout
    </div>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th>Course</th>
                    <th>Price</th>
                    <th>Quantity</th>
                    <th>Total</th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="item in cart.items"
                    :key="item.course.id"
                >
                    <td>{{ item.course.name }}</td>
                    <td>{{ item.course.price }}</td>
                    <td>{{ item.quantity }}</td>
                    <td>{{ getItemTotal(item).toFixed(2) }}$</td>
                </tr>
            </tbody>
            <tfoot>
                <tr>
                    <td colspan="2">Total</td>
                    <td>{{ cartTotalLength }}</td>
                    <td>{{ cartTotalPrice.toFixed(2) }}$</td>
                </tr>
            </tfoot>
        </table>
    </div>
    <div>
        <h2>Shipping details</h2>
        <div v-if="errors.length">
            <p
                v-for="error in errors"
                :key="error"
            >
                {{ error }}
            </p>
        </div>
        <div>
            <label>First name</label>
            <div>
                <input type="text" v-model="first_name">
            </div>
        </div>
        <div>
            <label>Last name</label>
            <div>
                <input type="text" v-model="last_name">
            </div>
        </div>
        <div>
            <label>Email</label>
            <div>
                <input type="text" v-model="email">
            </div>
        </div>
        <div>
            <label>phone</label>
            <div>
                <input type="text" v-model="phone">
            </div>
        </div>
    </div>
    <div>
        <div id="card-element"></div>
        <template v-if="cartTotalLength">
            <button @click="submitForm">Pay</button>
        </template>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            first_name: '',
            last_name: '',
            card: {},
            stripe: {},
            email: '',
            phone: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout'

        this.cart = this.$store.state.cart

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51H1HiuKBJV2qfWbD2gQe6aqanfw6Eyul5PO2KeOuSRlUMuaV4TxEtaQyzr9DbLITSZweL7XjK3p74swcGYrE2qEX00Hz7GmhMI')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })

            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.course.price
        },
        submitForm() {
            this.errors = []

            if (this.first_name === '') {
                this.errors.push('The first name field is missing')
            }

            if (this.last_name === '') {
                this.errors.push('The last name field is missing')
            }

            if (this.email === '') {
                this.errors.push('The email field is missing')
            }

            if (this.first_name === '') {
                this.errors.push('The phone field is missing')
            }

            if (!this.errors.length) {
                this.stripe.createToken(this.card).then(result => {
                    if (result.error) {
                        this.errors.push('Something went wrong')
                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
            const items = []

            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    course: item.course.id,
                    quantity: item.quantity,
                    price: item.course.price * item.quantity
                }

                items.push(obj)
            }

            const data = {
                'first_name' : this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id
            }

            await axios
                .post('/api/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Something went wrong')
                    console.log(error)
                })
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, currentValue) => {
                return acc += currentValue.course.price * currentValue.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, currentValue) => {
                return acc += currentValue.quantity
            }, 0)
        }
    }
}
</script>