<template>
  <h4 class="day-wise-plan">Day-wise plan</h4>
  <div class="d-flex" v-for="day in days" :key="day.id">
    <div class="flex-grow-1">
      <h5 class="day d-flex">
        <span class="day-text flex-shrink-0"
          >Day {{ day.order + 1 }}:&nbsp;</span
        >
        <InPlaceEditableInput
          inputType="input"
          placeholder="Write a title for you day"
          itemKey="name"
          :value="day.name"
          :editEndPoint="`/day/api/${day.id}/?itinerary_id=${itineraryId}`"
        />
      </h5>
      <p>
        <label for="notes">Notes</label>
        <InPlaceEditableInput
          :value="day.notes"
          inputType="textarea"
          placeholder="Write something about the day"
          :editEndPoint="`/day/api/${day.id}/?itinerary_id=${itineraryId}`"
          itemKey="notes"
        />
      </p>
      <br />
    </div>
    <div class="button-container flex-shrink-0">
      <button class="transparent-btn cross" @click="removeDay(day.id)">
        X
      </button>
      <button class="transparent-btn move-up" @click="moveDay(day.id, 'up')">
        ↑
      </button>
      <button
        class="transparent-btn move-down"
        @click="moveDay(day.id, 'down')"
      >
        ↓
      </button>
    </div>
  </div>
  <button class="green-btn" @click="addDay">Add Day</button>
</template>

<script>
import api from '@/api'
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'

export default {
  components: {
    InPlaceEditableInput,
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

.day {
  font-style: italic;
  display: flex;
  width: 100%;
}

/* Button Group */

.button-container {
  display: flex;
  flex-flow: column;
  padding-left: 4px;
}

.button-container button {
  background-color: white;
  border: none;
}
.cross {
  color: red;
}
</style>
