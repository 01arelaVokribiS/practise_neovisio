<template>
    <div>Log in</div>
    <form @submit.prevent="submitForm">
        <div v-if="errors.length">
            <p
                v-for="error in errors"
                :key="error"
            >
                {{ error }}
            </p>
        </div>
        <div>
            <label>Username</label>
            <div>
                <input type="text" v-model="username" placeholder="Enter username">
            </div>
        </div>
        <div>
            <label>Password</label>
            <div>
                <input type="password" v-model="password" placeholder="Enter password">
            </div>
        </div>
        <div>
            <div class="border-bottom">
                <router-link to="/sign-up">Sign up</router-link>
            </div>
            <div>
                <button>Log in</button>
            </div>
        </div>
    </form>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log in'
    },
    methods: {
        async submitForm() {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post('/api/token/login/', formData)
                .then(response => {
                    const token = response.data.auth_token

                    this.$store.commit('setToken', token)

                    axios.defaults.headers.common['Authorization'] = 'Token ' + token

                    localStorage.setItem('token', token)

                    const toPath = this.$route.query.to || '/cart'

                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            // this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong')
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>