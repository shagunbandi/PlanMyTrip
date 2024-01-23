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
          :editEndPoint="`/day/api/${day.id}/?itinerary_id=${itineraryId}`"
        />
      </h5>
      <span id="notes">
        <label for="notes">Notes</label>
        <InPlaceEditableInput
          :value="day.notes"
          inputType="textarea"
          placeholder="Write something about the day"
          :editEndPoint="`/day/api/${day.id}/?itinerary_id=${itineraryId}`"
          itemKey="notes"
        />
      </span>
      <br />

      <Dishes
        :dayId="day.id"
        :dishes="day.dishes"
        dishName="dish"
        dishTitle="Dish"
      />

      <!-- All other features go here -->
    </div>

    <div class="button-container flex-shrink-0">
      <button class="transparent-btn cross" @click="removeDay(day.id)">
        X
      </button>
      <button class="transparent-btn move-up" @click="moveDay(day.id, 'up')">
        ↑
      </button>
      <button
        class="transparent-btn move-down"
        @click="moveDay(day.id, 'down')"
      >
        ↓
      </button>
    </div>
  </div>
</template>

<script>
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'
import Dishes from '@/component/Itinerary/Dishes.vue'

export default {
  components: {
    InPlaceEditableInput,
    Dishes,
  },
  props: {
    itineraryId: Number,
    day: Object,
  },
  data() {
    return {}
  },
  emits: ['moveDay', 'removeDay'],
  methods: {
    removeDay(dayId) {
      this.$emit('removeDay', dayId)
    },
    moveDay(dayId, moveDirection) {
      this.$emit('moveDay', dayId, moveDirection)
    },
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
