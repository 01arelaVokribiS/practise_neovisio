<template>
    <header class="bg-dark">
        <nav class="navbar navbar-expand-md">
            <div class="container">
                <router-link to="/">Home</router-link>

                <a style="border: 1px solid red;" class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbar" aria-expanded="false">
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                    <span aria-hidden="true"></span>
                </a>

                <div class="collapse navbar-collapse" id="navbar">
                    <div
                        class="mx-2"
                        v-for="category in categories"
                        :key="category.id"
                    >
                        <router-link :to="category.get_absolute_url">{{ category.name }}</router-link>
                    </div>
                    <div class="d-flex align-items-center">
                        <router-link to="/cart" class="position-relative me-2">
                            <i class="fas fa-shopping-cart me-1"></i>
                            <span class="position-absolute  translate-middle badge rounded-pill">{{ cartTotalLength }}</span>
                        </router-link>
                        
                        <template v-if="$store.state.isAuthenticated">
                            <router-link to="/account">My account</router-link>
                        </template>
                        <template v-else>
                            <router-link to="/log-in">Log in</router-link>
                        </template>
                    </div>
                </div>
            </div>
        </nav>
    </header>
    <div class="container">
        <router-view/>
    </div>
    <footer>

    </footer>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            categories: [],
            cart: {
                items: []
            }
        }
    },
    beforeCreate() {
        this.$store.commit('initializeStore')

        const token = this.$store.state.token

        if (token) {
            axios.defaults.headers.common['Authorization'] = 'Token ' + token
        } else {
            axios.defaults.headers.common['Authorization'] = ''
        }
    },
    mounted() {
        this.getGategories()
        this.cart = this.$store.state.cart
    },
    computed: {
        cartTotalLength() {
            let totalLength = 0
            
            for (let i = 0; i < this.cart.items.length; i++) {
                totalLength += this.cart.items[i].quantity
            }

            return totalLength
        }
    },
    methods: {
        getGategories() {
            axios
                .get('/api/categories/')
                .then(response => {
                    this.categories = response.data

                    document.title = 'App'
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>

<style>
</style>
