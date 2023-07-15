<script>
import axios from 'axios'

export default {
  data() {
    return {
      distance: '',
      duration: ''
    }
  },

  props: {
    name: String,
    city: String,
    category: String,
    previous_item: Object,
    rating: Number,
    user_ratings_total: Number,
    location_name: String,
    place_id: String,
    time: String
  },

  methods: {
    getDistance() {
      console.log(this.previous_item, this.place_id)
      if (this.previous_item)
        axios
          .post('http://localhost:5000/maps/distance', {
            origin_place_id: this.place_id,
            destination_place_id: this.previous_item.details.place_id
          })
          .then((response) => {
            this.distance = response?.data?.response?.distance_in_meters
            this.duration = response?.data?.response?.time_in_minutes
          })
          .catch((error) => {
            console.log(error)
          })
    }
  },

  mounted() {
    this.getDistance()
  }
}
</script>

<template>
  <li>
    <span class="name">{{ name }}</span
    >, {{ city }}
    <br />
    <span class="category">{{ category }}</span>
    <br />
    {{ time }}
    <br />
    {{ rating }} / {{ user_ratings_total }} <br />
    Time to reach: {{ this.duration }} mins<br />
    Distance to cover: {{ this.distance }}m<br />
    <!-- {{ previous_item }}
    {{ place_id }} -->
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
