<template>
    <div class="container" v-if="users.length > 0">
        <item-list
            v-for="user in users"
            :key="user.id"
            :user="user"
        />
    </div>
    <div v-else>Empty list</div>
</template>

<script>
import ItemList from "@/components/ItemList";

export default {
    components: {
        ItemList,
    },
    props: {
        users: {
            type: Array,
            required: true
        }
    }
}
</script>

<style scoped>

</style>