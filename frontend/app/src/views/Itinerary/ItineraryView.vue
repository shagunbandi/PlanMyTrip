<template>
  <Container>
    <span v-if="itinerary">
      <Container>
        <!-- Title -->
        <h1 class="title">
          <PersistingInput
            :value="itinerary.title"
            inputType="input"
            :editEndPoint="`/api/planner/itinerary/${itinerary.id}/`"
            itemKey="title"
          />
        </h1>
        <h4 class="day-wise-plan">Itinerary</h4>
        <div v-for="day in itinerary.days" :key="day.id" class="d-flex">
          <Day :day="day" />
        </div>
        <button class="btn btn-success" @click="handleAddDay">Add Day</button>
      </Container>
    </span>

    <span v-else>
      <p>Loading itinerary...</p>
    </span>
  </Container>
</template>

<script>
import Container from '@/component/Container.vue'
import PersistingInput from '@/component/PersistingInput.vue'
import Day from '@/views/Itinerary/DayView.vue'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    Container,
    PersistingInput,
    Day,
  },
  data() {
    return {}
  },
  computed: {
    ...mapState('itinerary', ['itinerary']),
  },
  mounted() {
    this.fetchItinerary({
      itineraryId: 9,
      onSuccess: this.onSuccess,
      onError: this.onError,
    })
  },
  methods: {
    onSuccess(message) {
      this.$toast.success(message, { duration: 5000 })
    },
    onError(message) {
      this.$toast.error(message, { duration: 5000 })
    },
    handleAddDay() {
      this.addDay({ onSuccess: this.onSuccess, onError: this.onError })
    },
    ...mapActions('itinerary', ['fetchItinerary', 'addDay']),
  },
}
</script>

<style scoped>
.day-wise-plan {
  font-weight: bold;
}
</style>
