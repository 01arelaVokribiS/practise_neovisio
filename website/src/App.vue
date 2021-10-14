<template>
    <!-- modal window -->
    <custom-modal-window>
        <!-- users list -->
        <custom-list
            :users="users"
        />
    </custom-modal-window>
    <!-- form -->
    <custom-form
        @create="createUser"
    />
</template>

<script>
import CustomForm from "@/components/CustomForm";
import CustomList from "@/components/CustomList";

export default {
    components: {
        CustomForm,
        CustomList,
    },
    data() {
        return {
            users: [
                // { id: 1, surname: 'surname1', name: 'name1', username: 'username1', password: 'password1' },
            ],
        }
    },
    methods: {
        createUser(user) {
            this.users.push(user);
        }
    }
}
</script>

<style>

</style>