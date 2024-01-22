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
  emits: ['updateDays', 'fetchItinerary'],
  methods: {
    async addDay() {
      const newDayData = {
        name: 'New Day',
        notes: '',
      }
      try {
        const response = await api.post(
          `/day/api/?itinerary_id=${this.itineraryId}`,
          newDayData,
        )
        const newDay = response.data
        newDay.name = ''
        this.$emit('updateDays', [...this.days, response.data])
      } catch (error) {
        // Handle errors
        console.error('Error adding day:', error)
      }
    },
    async removeDay(dayId) {
      try {
        await api.delete(`day/api/${dayId}/?itinerary_id=${this.itineraryId}`)
        console.log('Day removed successfully:')
        this.$emit('fetchItinerary')
      } catch (error) {
        console.error('Error removing day:', error)
      }
    },
    async moveDay(dayId, moveDirection) {
      try {
        await api.post(
          `day/${this.itineraryId}/${dayId}/move/${moveDirection}/`,
        )
        console.log('Day moved successfully:')
        this.$emit('fetchItinerary')
      } catch (error) {
        console.error('Error moving day:', error)
      }
    },
  },
}
</script>

<style scoped>
/* Day Wise Plan */
.day-wise-plan {
  font-weight: bold;
}
</style>
