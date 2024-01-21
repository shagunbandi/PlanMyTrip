<template>
  <div>
    <div v-if="itinerary">
      <Container>
        <h1 class="title">
          <InPlaceEditableInput
            :value="itinerary.name"
            inputType="input"
            :editEndPoint="`/itinerary/api/${itineraryId}/`"
            itemKey="name"
          />
        </h1>
        <TitledTextInput
          v-if="itinerary.notes"
          title="Notes"
          :value="itinerary.notes"
          :editEndPoint="`/itinerary/api/${itineraryId}/`"
          itemKey="notes"
        />
        <TitledTextInput
          v-if="itinerary.scratchpad"
          title="Scratchpad"
          :value="itinerary.scratchpad"
          :editEndPoint="`/itinerary/api/${itineraryId}/`"
          itemKey="scratchpad"
        />
        <Container>
          <h4>Day-wise plan</h4>

          <span v-for="day in itinerary.days" :key="day.id">
            <Container>
              <h3>
                Day {{ day.order + 1
                }}<span v-if="day.name"
                  >:
                  <InPlaceEditableInput
                    :value="day.name"
                    inputType="input"
                    :editEndPoint="`/day/api/${day.id}/?itinerary_id=${itineraryId}`"
                    itemKey="name"
                /></span>
              </h3>
              <p>
                <InPlaceEditableInput
                  :value="day.notes"
                  inputType="textarea"
                  :editEndPoint="`/day/api/${day.id}/?itinerary_id=${itineraryId}`"
                  itemKey="notes"
                />
              </p>
            </Container>
            <!-- Display other details such as dishes, accommodations, restaurants, etc. as needed -->
          </span>
          <button class="green-button" @click="addDay">Add Day</button>
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
      itinerary: null,
      itineraryId: 1
    }
  },
  mounted() {
    // Fetch itinerary details when the component is mounted
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
    async addDay() {
      const newDayData = {
        name: 'New Day',
        notes: ''
      }
      try {
        const response = await api.post(`/day/api/?itinerary_id=${this.itineraryId}`, newDayData)
        this.itinerary.days = [...this.itinerary.days, response.data]
      } catch (error) {
        // Handle errors
        console.error('Error adding day:', error)
      }
    }
  }
}
</script>

<style scoped>
.title {
  text-align: center;
}
</style>
