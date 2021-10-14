<template>
    <div class="border rounded px-3 py-2 mb-1">
        <div>Surname: {{ user.surname }}</div>
        <div>Name: {{ user.name }}</div>
        <div>Username: {{ user.username }}</div>
        <div>Password: {{ user.password }}</div>
        <div>Country: {{ user.country }}</div>
    </div>
</template>

<script>
export default {
    props: {
        user: {
            type: Object,
            required: true
        }
    }
}
</script>

<style scoped>

</style>