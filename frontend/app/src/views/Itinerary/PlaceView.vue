<template>
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">{{ place.title }}</h5>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    place: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped></style>
