<template>
    <nav class="ps-1 pt-2">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="/" class="text-decoration-none">Home</a></li>
            <li class="breadcrumb-item"><a href="" class="text-decoration-none">Courses</a></li>
            <li class="breadcrumb-item active">{{ course.name }}</li>
        </ol>
    </nav>
    <div class="d-lg-flex justify-content-lg-between">
        <div class="mb-2 border p-3 col-lg-8">
            <div class="border-bottom mb-2">
                <h2>{{ course.name }}</h2>
            </div>
            <p>{{ course.description }}</p>
            <p v-if="!course.available">Сourse is not available</p>
            <p v-else>Available: {{ course.available }}</p>
            <img :src="course.get_image" class="pt-2 w-100" alt="course image">
        </div>
        <div class="col-lg-3">
            <div class="list-group border mb-2 p-4">
                <div class="d-flex justify-content-between mb-4 border-bottom">
                    <p>Price</p>
                    <p>{{ course.price }}$</p>
                </div>
                <div>
                    <input class="form-control" type="number" min="1" v-model="quantity">
                    <a class="btn btn-outline-dark" @click="addToCart"><i class="fas fa-cart-arrow-down me-2"></i>Add to cart</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Course',
    data() {
        return {
            course: {},
            quantity: 1,
        }
    },
    mounted() {
        this.getCourse()
    },
    methods: {
        getCourse() {
            const categorySlug = this.$route.params.category_slug
            const courseSlug = this.$route.params.course_slug

            axios
                .get(`/api/courses/${categorySlug}/${courseSlug}`)
                .then(response => {
                    this.course = response.data

                    document.title = this.course.name
                })
                .catch(error => {
                    console.log(error)
                })
        },
        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                course: this.course,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)
        }
    }
}
</script>

<style scoped>

</style>