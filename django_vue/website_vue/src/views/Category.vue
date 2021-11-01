<template>
    <div>{{ category.name }}</div>
    <CourseCard
        v-for="course in category.courses"
        :key="course.id"
        :course="course"
    />
</template>

<script>
import axios from 'axios';

import CourseCard from '@/components/CourseCard'

export default {
    name: 'Category',
    data() {
        return {
            category: {
                courses: [],
            }
        }
    },
    components: {
        CourseCard
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(to, from) {
            if (to.name === 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        getCategory() {
            const categorySlug = this.$route.params.category_slug

            axios
                .get(`/api/courses/${categorySlug}`)
                .then(response => {
                    this.category = response.data

                    document.title = this.category.name
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>