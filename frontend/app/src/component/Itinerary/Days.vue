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
  <button class="btn btn-success" @click="addDummyDay">Add Day</button>
</template>

<script>
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
    addDummyDay() {
      const newDayData = {
        name: 'New Day',
        notes: '',
      }
      this.addDay(newDayData)
    },
    ...mapActions('itinerary', [
      'fetchItinerary',
      'addDay',
      'removeDay',
      'moveDay',
    ]),
  },
}
</script>

<style scoped>
.day-wise-plan {
  font-weight: bold;
}
</style>
