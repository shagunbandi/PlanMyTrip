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
  }
})
</script>

<template>
  <li>
    <span class="name">{{ name }}</span
    >, {{ city }}
    <span class="category">{{ category }}</span>
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
