<template>
  <h4>Day-wise plan</h4>

  <span v-for="day in days" :key="day.id">
    <Container>
      <h3>
        Day {{ day.order + 1 }}:
        <InPlaceEditableInput
          inputType="input"
          placeholder="Write a title for you day"
          itemKey="name"
          :value="day.name"
          :editEndPoint="`/day/api/${day.id}/?itinerary_id=${itineraryId}`"
        />
      </h3>
      <p>
        <InPlaceEditableInput
          :value="day.notes"
          inputType="textarea"
          :editEndPoint="`/day/api/${day.id}/?itinerary_id=${itineraryId}`"
          itemKey="notes"
        />
      </p>
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
    </Container>
    <!-- Display other details such as dishes, accommodations, restaurants, etc. as needed -->
  </span>
  <button class="green-btn" @click="addDay">Add Day</button>
</template>

<script>
import api from '@/api'
import Container from '@/component/Container.vue'
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'

export default {
  components: {
    Container,
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
.cross {
  color: red;
  position: absolute;
  top: 10px;
  right: 10px;
  z-index: 1;
}

.move-up {
  color: white;
  position: absolute;
  top: 30px;
  right: 10px;
  z-index: 1;
}

.move-down {
  color: white;
  position: absolute;
  top: 50px;
  right: 10px;
  z-index: 1;
}
</style>
