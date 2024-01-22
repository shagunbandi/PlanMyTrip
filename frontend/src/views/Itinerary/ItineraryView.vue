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

        <Container>
          <h4>Day-wise plan</h4>

          <span v-for="day in itinerary.days" :key="day.id">
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
              <button
                class="transparent-btn move-up"
                @click="moveDay(day.id, 'up')"
              >
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
        </Container>
      </Container>
    </span>

    <span v-else>
      <p>Loading itinerary...</p>
    </span>
  </Container>
</template>

<script>
import api from '../../api'
import Container from '../../component/Container.vue'
import InPlaceEditableInput from '../../component/InPlaceEditableInput.vue'
import Notes from '../../component/Itinerary/Notes.vue'
import Scratchpad from '../../component/Itinerary/Scratchpad.vue'

export default {
  components: {
    Container,
    InPlaceEditableInput,
    Notes,
    Scratchpad,
  },
  data() {
    return {
      itinerary: null,
      itineraryId: 1,
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
        notes: '',
      }
      try {
        const response = await api.post(
          `/day/api/?itinerary_id=${this.itineraryId}`,
          newDayData,
        )
        this.itinerary.days = [...this.itinerary.days, response.data]
      } catch (error) {
        // Handle errors
        console.error('Error adding day:', error)
      }
    },
    async removeDay(dayId) {
      try {
        await api.delete(`day/api/${dayId}/?itinerary_id=${this.itineraryId}`)
        console.log('Day removed successfully:')
        this.fetchItinerary()
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
        this.fetchItinerary()
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
