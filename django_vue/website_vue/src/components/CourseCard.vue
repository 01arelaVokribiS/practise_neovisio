<template>
    <div class="row d-flex justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-12 pb-2">
            <div class="card shadow-sm">
                <img
                    :src="course.get_image"
                    alt="card image"
                    style="height: 200px; object-fit: cover;"
                >
                <div class="card-body">
                    <p class="card-text">{{ course.name }}</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <router-link :to="course.get_absolute_url">Details</router-link>
                        <label>{{ course.price }}$</label>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'CourseCard',
    props: {
        course: Object
    }
}
</script>