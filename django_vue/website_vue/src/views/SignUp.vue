<template>
    <div>SignUp</div>
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
            <label>Repeat password</label>
            <div>
                <input type="password" v-model="password2" placeholder="Repeat password">
            </div>
        </div>
        <div>
            <div class="border-bottom">If u  have acc, please
                <router-link to="/log-in">Log in</router-link>
            </div>
            <div>
                <button>Sign up</button>
            </div>
        </div>
    </form>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            password2: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Sign up'
    },
    methods: {
        submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is missing')
            }

            if (this.password === '') {
                this.errors.push('The password is too short')
            }

            if (this.password !== this.password2) {
                this.errors.push('The passwords doesn\'t match')
            }

            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password 
                }

                axios
                    .post('/api/users/', formData)
                    .then(response => {
                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }

                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong')

                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>