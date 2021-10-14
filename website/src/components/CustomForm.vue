<template>
    <div class="container">
        <form class="form border rounded col-lg-6 col-md-9 p-4 row g-2" @submit.prevent>
            <h4>User registration</h4>
            <div class="col-lg-6 col-md-6">
                <label class="form-label">Surname</label>
                <custom-input
                    v-model="user.surname"
                    placeholder="Enter surname"
                />
            </div>
            <div class="col-lg-6 col-md-6">
                <label class="form-label">Name</label>
                <custom-input
                    v-model="user.name"
                    placeholder="Enter name"
                />
            </div>
            <div class="col-12">
                <label class="form-label">Username</label>
                <custom-input
                    v-model="user.username"
                    placeholder="Enter username"
                />
            </div>
            <div class="col-12">
                <label class="form-label">Password</label>
                <custom-input
                    v-model="user.password"
                    type="password"
                    placeholder="Enter password"
                />
            </div>
            <div class="col-12">
                <label class="form-label">Country</label>
                <custom-select
                    v-model="user.country"
                    :options="selectOptions"
                />
            </div>
            <button class="btn btn-primary" @click="createUser">Submit</button>
            <small>v1.0</small>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            user: {
                surname: '',
                name: '',
                username: '',
                password: '',
                country: '',
            },
            selectOptions: [
                { value: 'Belarus', name: 'Belarus' },
                { value: 'Russia', name: 'Russia' },
            ]
        }
    },
    methods: {
        createUser() {
            this.user.id = Date.now();
            this.$emit('create', this.user);
            this.user = {
                surname: '',
                name: '',
                username: '',
                password: '',
                country: '',
            }
        }
    }
}
</script>

<style scoped>
.form { margin: 0 auto; }
</style>