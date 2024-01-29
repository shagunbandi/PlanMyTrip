<template>
  <Container>
    <span v-if="itinerary">
      <Container>
        <h1 class="title">
          <InPlaceEditableInput
            :value="itinerary.name"
            inputType="input"
            :editEndPoint="`/api/itinerary/${itineraryId}/`"
            itemKey="name"
          />
        </h1>
        <Notes :value="itinerary.notes" :itineraryId="itineraryId" />
        <br />
        <Scratchpad :value="itinerary.scratchpad" :itineraryId="itineraryId" />
        <br />
        <Days
          :itineraryId="itineraryId"
          :days="itinerary.days"
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
import Days from '@/component/Itinerary/Days.vue'
import Notes from '@/component/Itinerary/Notes.vue'
import Scratchpad from '@/component/Itinerary/Scratchpad.vue'

export default {
  components: {
    Container,
    InPlaceEditableInput,
    Notes,
    Scratchpad,
    Days,
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
        .get(`/api/itinerary/${this.itineraryId}/`)
        .then((response) => {
          this.itinerary = response.data
        })
        .catch((error) => {
          console.error('Error fetching itinerary:', error)
        })
    },
  },
}
</script>
