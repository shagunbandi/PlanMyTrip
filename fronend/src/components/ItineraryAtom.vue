<script setup>
defineProps({
  name: {
    type: String,
    required: true
  },
  city: {
    type: String,
    required: true
  },
  category: {
    type: String,
    required: true
  },
  rating: {
    type: Float32Array,
    required: false
  },
  user_ratings_total: {
    type: Number,
    required: false
  }
})
</script>

<template>
  <li>
    <span class="name">{{ name }}</span
    >, {{ city }} <span class="category">{{ category }}</span
    ><br />
    {{ rating }} / {{ user_ratings_total }}
  </li>
</template>

<style scoped>
li {
  margin-bottom: 20px;
}

.name {
  font-size: x-large;
  font-weight: bold;
}

.category {
  font-style: italic;
  background-color: lightblue;
}
</style>
