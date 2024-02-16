<template>
  <Container>
    <span v-if="itinerary">
      <Container>
        <!-- Title -->
        <h1 class="title">
          <PersistingInput
            :value="itinerary.name"
            inputType="input"
            :editEndPoint="`/api/itinerary/${itinerary.id}/`"
            itemKey="name"
          />
        </h1>

        <!-- Notes -->
        <label for="notes">Notes</label>

        <PersistingEditorInput
          title="Notes"
          itemKey="notes"
          :value="itinerary.notes"
          :editEndPoint="`/api/itinerary/${itinerary.id}/`"
          placeholder="Notes here"
        />

        <br />

        <!-- Scratchpad -->
        <label for="scratchpad">ScratchPad</label>
        <PersistingEditorInput
          title="ScratchPad"
          :value="itinerary.scratchpad"
          :editEndPoint="`/api/itinerary/${itinerary.id}/`"
          itemKey="scratchpad"
          placeholder="Write your thoughts here"
        />

        <br />

        <!-- Day Wise Plan -->
        <!-- <h4 class="day-wise-plan">Day-wise plan</h4>
        <div v-for="day in itinerary.days" :key="day.id" class="d-flex">
          <Day :day="day" />
        </div>
        <button class="btn btn-success" @click="addDummyDay">Add Day</button>
        -->
      </Container>
    </span>

    <span v-else>
      <p>Loading itinerary...</p>
    </span>
  </Container>
</template>

<script>
import Container from '@/component/Container.vue'
import PersistingEditorInput from '@/component/PersistingEditorInput.vue'
import PersistingInput from '@/component/PersistingInput.vue'
import Day from '@/views/Itinerary/DayView.vue'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    Container,
    PersistingInput,
    Day,
    PersistingEditorInput,
  },
  data() {
    return {}
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
