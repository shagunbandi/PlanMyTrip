<template>
  <SideActionPannel
    :buttons="[
      { text: '↑', clickHandler: () => handleMoveDay('up') },
      { text: '↓', clickHandler: () => handleMoveDay('down') },
      {
        text: 'X',
        clickHandler: handleRemoveDay,
        style: { color: 'red' },
      },
    ]"
  >
    <div class="flex-grow-1">
      <!-- Day Title -->
      <h5 id="day-title" class="day d-flex">
        <span class="day-text flex-shrink-0"
          >Day {{ day.order + 1 }}:&nbsp;</span
        >
        <PersistingInput
          inputType="input"
          placeholder="Write a title for you day"
          itemKey="title"
          :value="day.title"
          :editEndPoint="`/api/planner/itinerary/${itinerary.id}/day/${day.id}/`"
        />
      </h5>
    </div>
  </SideActionPannel>
</template>

<script>
import PersistingInput from '@/component/PersistingInput.vue'
import SideActionPannel from '@/component/SideActionPannel.vue'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    PersistingInput,
    SideActionPannel,
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
    onSuccess(message) {
      this.$toast.success(message, { duration: 5000 })
    },
    onError(message) {
      this.$toast.error(message, { duration: 5000 })
    },
    handleMoveDay(direction) {
      this.moveDay({
        dayId: this.day.id,
        direction: direction,
        onSuccess: this.onSuccess,
        onError: this.onError,
      })
    },
    handleRemoveDay() {
      this.removeDay({
        dayId: this.day.id,
        onSuccess: this.onSuccess,
        onError: this.onError,
      })
    },
    ...mapActions('itinerary', ['removeDay', 'moveDay']),
  },
}
</script>

<style scoped></style>
