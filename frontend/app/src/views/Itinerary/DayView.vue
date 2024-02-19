<template>
  <SideActionPannel
    :buttons="[
      {
        text: '↑',
        clickHandler: () => handleMoveDay('up'),
      },
      {
        text: '↓',
        clickHandler: () => handleMoveDay('down'),
      },
      {
        text: 'X',
        clickHandler: handleRemoveDay,
        style: { color: 'red' },
      },
      { type: 'break' },
      {
        type: 'icon',
        src: addDayIcon,
        clickHandler: handleAddPlace,
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
      <Container>
        <span v-for="place in day.places" :key="place.id" class="d-flex">
          <PlaceView :place="place" />
        </span>
      </Container>
    </div>
  </SideActionPannel>
</template>

<script>
import AddDayIcon from '@/assets/icons/add-day-icon.png'
import Container from '@/component/Container.vue'
import PersistingInput from '@/component/PersistingInput.vue'
import SideActionPannel from '@/component/SideActionPannel.vue'
import { mapActions, mapState } from 'vuex'
import PlaceView from './PlaceView.vue'

export default {
  components: {
    PersistingInput,
    SideActionPannel,
    Container,
    PlaceView,
  },
  props: {
    day: Object,
  },
  computed: {
    ...mapState('itinerary', ['itinerary']),
  },
  data() {
    return {
      addDayIcon: AddDayIcon,
    }
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
    handleAddPlace() {},
    ...mapActions('itinerary', ['removeDay', 'moveDay']),
  },
}
</script>

<style scoped></style>
