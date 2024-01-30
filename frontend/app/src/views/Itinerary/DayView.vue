<template>
  <div class="flex-grow-1">
    <h5 id="day-name" class="day d-flex">
      <span class="day-text flex-shrink-0">Day {{ day.order + 1 }}:&nbsp;</span>
      <InPlaceEditableInput
        inputType="input"
        placeholder="Write a title for you day"
        itemKey="name"
        :value="day.name"
        :editEndPoint="`/api/day/${day.id}/?itinerary_id=${itinerary.id}`"
      />
    </h5>
    <span id="notes">
      <label for="notes">Notes</label>
      <InPlaceEditableInput
        :value="day.notes"
        inputType="textarea"
        placeholder="Write something about the day"
        :editEndPoint="`/api/day/${day.id}/?itinerary_id=${itinerary.id}`"
        itemKey="notes"
      />
    </span>
    <br />
    <DetailView
      :dayId="day.id"
      :details="day.dishes"
      name="dish"
      title="Dish"
    />
    <DetailView
      :dayId="day.id"
      :details="day.accomodations"
      name="accomodation"
      title="Accomodation"
    />

    <DetailView
      :dayId="day.id"
      :details="day.restaurants"
      name="restaurant"
      title="Restaurant"
    />

    <DetailView
      :dayId="day.id"
      :details="day.attractions"
      name="attraction"
      title="Attraction"
      :newDetailData="newAttraction"
    />

    <!-- All other features go here -->
  </div>

  <div class="button-container flex-shrink-0">
    <button class="cross" @click="removeDay(day.id)">X</button>
    <button
      class="move-up"
      @click="moveDay({ dayId: day.id, moveDirection: 'up' })"
    >
      ↑
    </button>
    <button
      class="move-down"
      @click="moveDay({ dayId: day.id, moveDirection: 'down' })"
    >
      ↓
    </button>
  </div>
</template>

<script>
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'
import { ATTRACTION_ENUM } from '@/constants'
import { mapActions, mapState } from 'vuex'
import DetailView from './DetailView.vue'

export default {
  components: {
    InPlaceEditableInput,
    DetailView,
  },
  props: {
    day: Object,
  },
  computed: {
    ...mapState('itinerary', ['itinerary']),
  },
  data() {
    return {
      newAttraction: {
        name: 'New Attraction',
        notes: '',
        category: ATTRACTION_ENUM.EXPERIENCE,
      },
    }
  },
  methods: {
    ...mapActions('itinerary', ['fetchItinerary', 'removeDay', 'moveDay']),
  },
}
</script>

<style scoped>
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
