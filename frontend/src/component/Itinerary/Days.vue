<template>
  <h4 class="day-wise-plan">Day-wise plan</h4>
  <Day
    v-for="day in days"
    :key="day.id"
    :itineraryId="itineraryId"
    :day="day"
    @moveDay="moveDay"
    @removeDay="removeDay"
    @fetchItinerary="fetchItinerary"
  />
  <button class="btn btn-success" @click="addDay">Add Day</button>
</template>

<script>
import api from '@/api'
import Day from '@/component/Itinerary/Day.vue'

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
  emits: ['fetchItinerary'],
  methods: {
    async addDay() {
      const newDayData = {
        name: 'New Day',
        notes: '',
      }
      try {
        await api.post(`/day/api/?itinerary_id=${this.itineraryId}`, newDayData)
        this.fetchItinerary()
      } catch (error) {
        console.error('Error adding day:', error)
      }
    },
    async removeDay(dayId) {
      try {
        await api.delete(`day/api/${dayId}/?itinerary_id=${this.itineraryId}`)
        this.fetchItinerary()
      } catch (error) {
        console.error('Error removing day:', error)
      }
    },
    async moveDay(dayId, moveDirection) {
      try {
        await api.post(
          `day/${this.itineraryId}/${dayId}/move/${moveDirection}/`,
        )
        this.fetchItinerary()
      } catch (error) {
        console.error('Error moving day:', error)
      }
    },
    fetchItinerary() {
      this.$emit('fetchItinerary')
    },
  },
}
</script>

<style scoped>
.day-wise-plan {
  font-weight: bold;
}
</style>
