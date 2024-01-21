<template>
  <div>
    <div v-if="itinerary">
      <Container>
        <h1 class="title">
          <InPlaceEditableInput
            :value="itinerary.name"
            inputType="input"
            editEndPoint="/itinerary/api/1/"
            itemKey="name"
          />
        </h1>
        <TitledTextInput
          v-if="itinerary.notes"
          title="Notes"
          :value="itinerary.notes"
          editEndPoint="/itinerary/api/1/"
          itemKey="notes"
        />
        <TitledTextInput
          v-if="itinerary.scratchpad"
          title="Scratchpad"
          :value="itinerary.scratchpad"
          editEndPoint="/itinerary/api/1/"
          itemKey="scratchpad"
        />
        <Container>
          <h4>Day-wise plan</h4>

          <span v-for="day in itinerary.days" :key="day.id">
            <Container>
              <h3>
                Day {{ day.order + 1
                }}<span v-if="day.name"
                  >: <InPlaceEditableInput :value="day.name" inputType="input"
                /></span>
              </h3>
              <p>{{ day.notes }}</p>
            </Container>
            <!-- Display other details such as dishes, accommodations, restaurants, etc. as needed -->
          </span>
        </Container>
      </Container>
    </div>

    <div v-else>
      <p>Loading itinerary...</p>
    </div>
  </div>
</template>

<script>
import api from '../../api'
import Container from '../../component/Container.vue'
import TitledTextInput from '../../component/TitledTextInput.vue'
import InPlaceEditableInput from '../../component/InPlaceEditableInput.vue'

export default {
  components: {
    Container,
    TitledTextInput,
    InPlaceEditableInput
  },
  data() {
    return {
      itinerary: null
    }
  },
  mounted() {
    // Fetch itinerary details when the component is mounted
    this.fetchItinerary()
  },
  methods: {
    fetchItinerary() {
      api
        .get('/itinerary/api/1')
        .then((response) => {
          this.itinerary = response.data
          console.log(this.itinerary)
        })
        .catch((error) => {
          console.error('Error fetching itinerary:', error)
        })
    }
  }
}
</script>

<style scoped>
.title {
  text-align: center;
}
</style>
