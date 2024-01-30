<template>
  <h4 class="day-wise-plan">Day-wise plan</h4>
  <Day
    v-for="day in days"
    :key="day.id"
    :itineraryId="itineraryId"
    :day="day"
    @moveDay="moveDay"
    @removeDay="removeDay"
  />
  <button class="btn btn-success" @click="addDay">Add Day</button>
</template>

<script>
import api from '@/api'
import Day from '@/component/Itinerary/Day.vue'
import { mapActions } from 'vuex'

export default {
  components: {
    Day,
  },
  props: {
    itineraryId: Number,
    days: Object,
  },
  data() {
    return {}
  },
  methods: {
    async addDay() {
      const newDayData = {
        name: 'New Day',
        notes: '',
      }
      try {
        await api.post(`/api/itinerary/${this.itineraryId}/day/`, newDayData)
        this.fetchItinerary()
      } catch (error) {
        console.error('Error adding day:', error)
      }
    },
    async removeDay(dayId) {
      try {
        await api.delete(`/api/itinerary/${this.itineraryId}/day/${dayId}/`)
        this.fetchItinerary()
      } catch (error) {
        console.error('Error removing day:', error)
      }
    },
    async moveDay(dayId, moveDirection) {
      try {
        await api.post(
          `/api/itinerary/${this.itineraryId}/day/${dayId}/move/${moveDirection}/`,
        )
        this.fetchItinerary()
      } catch (error) {
        console.error('Error moving day:', error)
      }
    },
    ...mapActions('itinerary', ['fetchItinerary']),
  },
}
</script>

<style scoped>
.day-wise-plan {
  font-weight: bold;
}
</style>
