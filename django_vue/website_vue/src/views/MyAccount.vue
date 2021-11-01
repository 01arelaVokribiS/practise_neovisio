<template>
    <div>
        <button @click="logout()" class="btn btn-danger">Log out</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MyAccount',
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ''

            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$route.commit('removeToken')

            this.$route.push('/')
        }
    }
}
</script>