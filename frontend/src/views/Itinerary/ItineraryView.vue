<template>
  <Container>
    <span v-if="itinerary">
      <Container>
        <h1 class="title">
          <InPlaceEditableInput
            :value="itinerary.name"
            inputType="input"
            :editEndPoint="`/itinerary/api/${itineraryId}/`"
            itemKey="name"
          />
        </h1>

        <Notes :value="itinerary.notes" :itineraryId="itineraryId" />
        <Scratchpad :value="itinerary.scratchpad" :itineraryId="itineraryId" />
        <DayWisePlan
          :itineraryId="itineraryId"
          :days="itinerary.days"
          @updateDays="updateDays"
          @fetchItinerary="fetchItinerary"
        />
      </Container>
    </span>

    <span v-else>
      <p>Loading itinerary...</p>
    </span>
  </Container>
</template>

<script>
import api from '@/api'
import Container from '@/component/Container.vue'
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'
import DayWisePlan from '@/component/Itinerary/DayWisePlan.vue'
import Notes from '@/component/Itinerary/Notes.vue'
import Scratchpad from '@/component/Itinerary/Scratchpad.vue'

export default {
  components: {
    Container,
    InPlaceEditableInput,
    Notes,
    Scratchpad,
    DayWisePlan,
  },
  data() {
    return {
      itinerary: null,
      itineraryId: 1,
    }
  },
  mounted() {
    this.fetchItinerary()
  },
  methods: {
    fetchItinerary() {
      api
        .get(`/itinerary/api/${this.itineraryId}`)
        .then((response) => {
          this.itinerary = response.data
          console.log(this.itinerary)
        })
        .catch((error) => {
          console.error('Error fetching itinerary:', error)
        })
    },
    updateDays(newValue) {
      this.itinerary.days = newValue
    },
  },
}
</script>
