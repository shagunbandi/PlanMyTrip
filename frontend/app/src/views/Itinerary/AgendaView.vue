<template>
  <SideActionPannel
    :buttons="[
      {
        text: '↑',
        clickHandler: () => handleMoveAgenda('up'),
      },
      {
        text: '↓',
        clickHandler: () => handleMoveAgenda('down'),
      },
      {
        text: 'X',
        clickHandler: handleRemoveAgenda,
        style: { color: 'red' },
      },
      { type: 'break' },
      {
        type: 'icon',
        src: addAgendaIcon,
        clickHandler: handleAddPlace,
      },
    ]"
  >
    <!-- Agenda Title -->
    <h5 id="agenda-title" class="d-flex agenda-title">
      <span class="agenda-text flex-shrink-0"
        >Agenda {{ agenda.order + 1 }}:&nbsp;</span
      >
      <PersistingInput
        inputType="input"
        placeholder="Write a title for you agenda"
        itemKey="title"
        :value="agenda.title"
        :editEndPoint="`/api/planner/itinerary/${itinerary.id}/agenda/${agenda.id}/`"
      />
    </h5>
  </SideActionPannel>
  <span v-for="(place, index) in agenda.places" :key="place.id" class="">
    <PlaceView :place="place" :agendaId="agenda.id" />
  </span>
</template>

<script>
import AddAgendaIcon from '@/assets/icons/add-agenda-icon.png'
import PersistingInput from '@/component/PersistingInput.vue'
import SideActionPannel from '@/component/SideActionPannel.vue'
import { mapActions, mapState } from 'vuex'
import PlaceView from './PlaceView.vue'

export default {
  components: {
    PersistingInput,
    SideActionPannel,
    PlaceView,
  },
  props: {
    agenda: Object,
  },
  computed: {
    ...mapState('itinerary', ['itinerary']),
  },
  data() {
    return {
      addAgendaIcon: AddAgendaIcon,
    }
  },
  methods: {
    onSuccess(message) {
      this.$toast.success(message, { duration: 5000 })
    },
    onError(message) {
      this.$toast.error(message, { duration: 5000 })
    },
    handleMoveAgenda(direction) {
      this.moveAgenda({
        agendaId: this.agenda.id,
        direction: direction,
        onSuccess: this.onSuccess,
        onError: this.onError,
      })
    },
    handleRemoveAgenda() {
      this.removeAgenda({
        agendaId: this.agenda.id,
        onSuccess: this.onSuccess,
        onError: this.onError,
      })
    },
    handleAddPlace() {
      this.addPlace({
        agendaId: this.agenda.id,
        onSuccess: this.onSuccess,
        onError: this.onError,
      })
    },
    ...mapActions('itinerary', ['removeAgenda', 'moveAgenda', 'addPlace']),
  },
}
</script>

<style scoped>
.agenda-title {
  margin-top: 20px;
}
</style>
