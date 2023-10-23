<script>
import axios from 'axios'
import ItineraryAtom from '../components/ItineraryAtom.vue'
import DrawGoogleMap from '../components/DrawGoogleMap.vue'
// import find from '../utitlities/findPathCircular'

export default {
  name: 'PlanView',
  data() {
    return {
      items: [],
      totalDistance: 0,
      totalDuration: 0,
    }
  },
  components: {
    ItineraryAtom,
    DrawGoogleMap
  },
  methods: {
    sortedPoints(points) {
      return points
      // return find(
      //   points,
      //   (point) => point.location.lat,
      //   (point) => point.location.lng,
      //   0
      // )
    },
    getItems() {
      axios
        .post('http://localhost:8000/planner/', {
          is_mock: true,
          country: 'India',
          number_of_days: '15'
        })
        .then((response) => {
          
          this.items = this.sortedPoints(response?.data)
          this.totalDistance = this.items.reduce((acc, curr) => acc + curr.distance_in_meters, 0)
          this.totalDuration = this.items.reduce((acc, curr ) => acc + curr.duration_in_mins, 0)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  mounted() {
    this.getItems()
  }
}
</script>

<template>
  <div class="container">
    <ul class="itinerary-compound">
      <ItineraryAtom
        v-for="(item, index) in this.items"
        :key="index"
        :previous_item="index === 0 ? None : this.items[index - 1]"
        :city="item.city"
        :category="item.category"
        :name="item.name"
        :location_name="item.name"
        :location="item.location"
        :rating="item.rating"
        :user_ratings_total="item.user_ratings_total"
        :time="item.time"
        :place_id="item.place_id"
        :duration_in_mins="item.duration_in_mins"
        :distance_in_meters="item.distance_in_meters"
      />
    </ul>
    <div class="container-right">
      <!-- <span class="google-map-container-dummy"></span> -->

    <DrawGoogleMap
      class="google-map-container"
      v-if="this.items.length > 0"
      :markers="this.items.map((item) => item.location)"
    />
      <div class="info-boxes">
        <div>
          <h3>Total Distance </h3>
          {{ totalDistance }}
        </div>
        <div><h3>Total Duration </h3>
          {{ totalDuration }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.info-boxes {
  display: flex;
}

.info-boxes > div {
  flex: 1;
  background-color: #e6ffe6;
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
}

.info-boxes > div > h3 {
  /* margin-bottom: 0; */
  font-weight: bold;
}

.container {
  padding-top: 40px;
  display: flex;
}

.container-right {
  flex: 1;
  width: 100%;
  height: 100%;
}
.google-map-container-dummy {
  background-color: greenyellow;
  display: flex;
  height: 400px;
  width: 100%;
}

 
.google-map-container {
  width: 100%;
  border-radius: 20px;
  overflow: hidden;
}

.itinerary-compound {
  list-style-type: none;
  padding: 0;
  flex: 1
}

</style>