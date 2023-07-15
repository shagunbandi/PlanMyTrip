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
    type: Number,
    required: false
  },
  user_ratings_total: {
    type: Number,
    required: false
  },
  location_name: {
    type: String,
    required: false
  },
  time: {
    type: String,
    required: false
  },
  place_id: {
    type: String,
    required: false
  },
  previous_item: {
    type: Object,
    required: false
  }
})
</script>

<!-- <script>
import axios from 'axios'

axios
  .post('http://localhost:5000/maps/distance', {
    is_prompt: false,
    country: 'India',
    number_of_days: '2'
  })
  .then((response) => {
    this.items = response?.data?.response?.content
  })
  .catch((error) => {
    console.log(error)
  })
</script> -->

<template>
  <li>
    <span class="name">{{ name }}</span
    >, {{ city }}
    <br />
    <span class="category">{{ category }}</span>
    <br />
    {{ time }}
    <br />
    {{ rating }} / {{ user_ratings_total }}
    {{ previous_item }}
    {{ place_id }}
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
