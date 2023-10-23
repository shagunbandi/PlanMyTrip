<script>
// import axios from 'axios'

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
    time: String,
    duration_in_mins: Number,
    distance_in_meters: Number
  },

  methods: {
    getDistance() {
      // if (this.previous_item)
      //   axios
      //     .post('http://localhost:8000/maps/distance', {
      //       origin_place_id: this.place_id,
      //       destination_place_id: this.previous_item.place_id
      //     })
      //     .then((response) => {
      //       this.distance = response?.data?.response?.distance_in_meters
      //       this.duration = response?.data?.response?.duration_in_mins
      //     })
      //     .catch((error) => {
      //       console.log(error)
      //     })
    }
  },

  mounted() {
    this.getDistance()
  }
}
</script>

<template>
  <li class="itinerary-atom">
    <div class="content">
      <span class="name">{{ name }}</span
      >, {{ city }}
      <br />
      <span class="category">{{ category }}</span>
      <br />
      {{ time }}
      <br />
      {{ rating }} / {{ user_ratings_total }} <br />
      Time to reach: {{ duration_in_mins }} mins<br />
      Distance to cover: {{ distance_in_meters }}m<br />
    </div>
  </li>
</template>

<style scoped>

.itinerary-atom {
  padding: 10px;
  margin-bottom: 0;
}
.itinerary-atom > .content {
background-color: #e6e6ff;
border-radius: 20px;
padding: 20px;
}

li {
  margin-bottom: 20px;
}

.name {
  font-size: x-large;
  font-weight: bold;
}

.category {
  font-style: italic;
  background-color: lightcyan;
}
</style>
