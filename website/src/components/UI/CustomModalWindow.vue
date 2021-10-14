<template>
    <div class="container">
        <!-- trigger button -->
        <button type="button" class="btn btn-primary my-3" data-bs-toggle="modal" data-bs-target="#modal">
            Users list
        </button>
    </div>

    <!-- modal window with users list -->
    <div class="modal fade" id="modal" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
            <div class="modal-content">
                <!-- modal header -->
                <div class="modal-header">
                    <h5 class="modal-title" id="modalLabel">Users list</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <!-- modal body -->
                <div class="modal-body">
                    <slot></slot>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'custom-modal-window'
}
</script>

<style scoped>
.btn {
    position: relative;
    left: 25%;
}

@media (max-width: 991.98px) {
    .btn { left: 12.5%; }
}

@media (max-width: 767.98px) {
    .btn { left: 0; }
}
</style>
