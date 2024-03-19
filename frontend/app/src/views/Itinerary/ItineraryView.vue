<template>
  <Container>
    <span v-if="itinerary">
      <Container>
        <!-- Title -->
        <h1 class="title">
          <PersistingInput
            :value="itinerary.title"
            inputType="input"
            :editEndPoint="`/api/planner/itinerary/${itinerary.id}/`"
            itemKey="title"
          />
        </h1>
        <h4 class="agenda-wise-plan">Itinerary</h4>
        <div v-for="agenda in itinerary.agendas" :key="agenda.id">
          <Agenda :agenda="agenda" />
        </div>
        <button class="btn btn-success" @click="handleAddAgenda">
          Add Agenda
        </button>
      </Container>
    </span>

    <span v-else>
      <p>Loading itinerary...</p>
    </span>
  </Container>
</template>

<script>
import Container from '@/component/Container.vue'
import PersistingInput from '@/component/PersistingInput.vue'
import Agenda from '@/views/Itinerary/AgendaView.vue'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    Container,
    PersistingInput,
    Agenda,
  },
  data() {
    return {}
  },
  computed: {
    ...mapState('itinerary', ['itinerary']),
  },
  mounted() {
    this.fetchItinerary({
      itineraryId: 1,
      onSuccess: this.onSuccess,
      onError: this.onError,
    })
  },
  methods: {
    onSuccess(message) {
      this.$toast.success(message, { duration: 5000 })
    },
    onError(message) {
      this.$toast.error(message, { duration: 5000 })
    },
    handleAddAgenda() {
      this.addAgenda({ onSuccess: this.onSuccess, onError: this.onError })
    },
    ...mapActions('itinerary', ['fetchItinerary', 'addAgenda']),
  },
}
</script>

<style scoped>
.title {
  font-weight: bolder;
}
.agenda-wise-plan {
  font-weight: bold;
  margin-top: 16px;
}
</style>
