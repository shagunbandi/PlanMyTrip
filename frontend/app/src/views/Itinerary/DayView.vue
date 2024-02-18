<template>
  <div class="flex-grow-1">
    <!-- Day Title -->
    <h5 id="day-title" class="day d-flex">
      <span class="day-text flex-shrink-0">Day {{ day.order + 1 }}:&nbsp;</span>
      <PersistingInput
        inputType="input"
        placeholder="Write a title for you day"
        itemKey="title"
        :value="day.title"
        :editEndPoint="`/api/planner/itinerary/${itinerary.id}/day/${day.id}/`"
      />
    </h5>
  </div>
</template>

<script>
import PersistingInput from '@/component/PersistingInput.vue'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    PersistingInput,
  },
  props: {
    day: Object,
  },
  computed: {
    ...mapState('itinerary', ['itinerary']),
  },
  data() {
    return {}
  },
  methods: {
    ...mapActions('itinerary', ['fetchItinerary', 'removeDay', 'moveDay']),
  },
}
</script>

<style scoped></style>
