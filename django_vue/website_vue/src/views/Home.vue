<template>
    <CourseCard
        v-for="course in courses"
        :key="course.id"
        :course=course
    />
</template>

<script>
import axios from 'axios'

import CourseCard from '@/components/CourseCard'

export default {
    name: 'Home',
    data() {
        return {
            courses: []
        }
    },
    components: {
        CourseCard
    },
    mounted() {
        this.getCourses()

        document.title = 'Home'
    },
    methods: {
        getCourses() {
            axios
                .get('/api/courses/')
                .then(response => {
                    this.courses = response.data
                })
                .catch(error => {
                    console.log(error);
                })
        }
    }
}
</script>
