<template>
  <div class="d-flex">
    <div class="flex-grow-1">
      <h5 id="day-name" class="day d-flex">
        <span class="day-text flex-shrink-0"
          >Day {{ day.order + 1 }}:&nbsp;</span
        >
        <InPlaceEditableInput
          inputType="input"
          placeholder="Write a title for you day"
          itemKey="name"
          :value="day.name"
          :editEndPoint="`/api/day/${day.id}/?itinerary_id=${itineraryId}`"
        />
      </h5>
      <span id="notes">
        <label for="notes">Notes</label>
        <InPlaceEditableInput
          :value="day.notes"
          inputType="textarea"
          placeholder="Write something about the day"
          :editEndPoint="`/api/day/${day.id}/?itinerary_id=${itineraryId}`"
          itemKey="notes"
        />
      </span>
      <br />
      <Detail :dayId="day.id" :details="day.dishes" name="dish" title="Dish" />
      <Detail
        :dayId="day.id"
        :details="day.accomodations"
        name="accomodation"
        title="Accomodation"
      />

      <Detail
        :dayId="day.id"
        :details="day.restaurants"
        name="restaurant"
        title="Restaurant"
      />

      <Detail
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
      <button class="move-up" @click="moveDay(day.id, 'up')">↑</button>
      <button class="move-down" @click="moveDay(day.id, 'down')">↓</button>
    </div>
  </div>
</template>

<script>
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'
import Detail from '@/component/Itinerary/Detail.vue'
import { ATTRACTION_ENUM } from '@/constants'
import { mapActions } from 'vuex'

export default {
  components: {
    InPlaceEditableInput,
    Detail,
  },
  props: {
    itineraryId: Number,
    day: Object,
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
  emits: ['moveDay', 'removeDay'],
  methods: {
    removeDay(dayId) {
      this.$emit('removeDay', dayId)
    },
    moveDay(dayId, moveDirection) {
      this.$emit('moveDay', dayId, moveDirection)
    },
    ...mapActions('itinerary', ['fetchItinerary']),
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
