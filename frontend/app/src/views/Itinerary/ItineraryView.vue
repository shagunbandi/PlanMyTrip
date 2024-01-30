<template>
  <Container>
    <span v-if="itinerary">
      <Container>
        <!-- Title -->
        <h1 class="title">
          <InPlaceEditableInput
            :value="itinerary.name"
            inputType="input"
            :editEndPoint="`/api/itinerary/${itineraryId}/`"
            itemKey="name"
          />
        </h1>

        <!-- Notes -->
        <Notes :value="itinerary.notes" :itineraryId="itineraryId" />
        <br />

        <!-- Scratchpad -->
        <Scratchpad :value="itinerary.scratchpad" :itineraryId="itineraryId" />
        <br />

        <!-- Day Wise Plan -->
        <h4 class="day-wise-plan">Day-wise plan</h4>
        <div v-for="day in itinerary.days" :key="day.id" class="d-flex">
          <Day :day="day" />
        </div>
        <button class="btn btn-success" @click="addDummyDay">Add Day</button>
      </Container>
    </span>

    <span v-else>
      <p>Loading itinerary...</p>
    </span>
  </Container>
</template>

<script>
import Container from '@/component/Container.vue'
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'
import Notes from '@/component/Itinerary/Notes.vue'
import Scratchpad from '@/component/Itinerary/Scratchpad.vue'
import Day from '@/views/Itinerary/DayView.vue'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    Container,
    InPlaceEditableInput,
    Notes,
    Scratchpad,
    Day,
  },
  data() {
    return {
      itineraryId: 1,
    }
  },
  computed: {
    ...mapState('itinerary', ['itinerary']),
  },
  mounted() {
    this.fetchItinerary()
  },
  methods: {
    addDummyDay() {
      this.addDay({
        name: 'New Day',
        notes: '',
      })
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
