<template>
  <Container>
    <span v-if="plan">
      <Container>
        <!-- Title -->
        <h1 class="title">
          <PersistingInput
            :value="plan.title"
            inputType="input"
            :editEndPoint="`/api/planner/plan/${plan.id}/`"
            itemKey="title"
          />
        </h1>

        <!-- List -->
        <Agenda
          v-for="agenda in filteredList"
          :key="agenda.id"
          :agenda="agenda"
        />
        <button
          class="btn btn-success"
          @click="() => handleAddAgenda({ is_itinerary: false })"
        >
          Add List
        </button>

        <!-- Plan -->
        <h4 class="agenda-wise-plan">Plan</h4>
        <Agenda
          v-for="(agenda, index) in filteredDays"
          :key="agenda.id"
          :agenda="agenda"
          :dayNum="index + 1"
        />
        <button
          class="btn btn-success"
          @click="() => handleAddAgenda({ is_itinerary: true })"
        >
          Add Day
        </button>
      </Container>
    </span>

    <span v-else>
      <p>Loading plan...</p>
    </span>
  </Container>
</template>

<script>
import Container from '@/component/Container.vue'
import PersistingInput from '@/component/PersistingInput.vue'
import Agenda from '@/views/Plan/AgendaView.vue'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    Container,
    PersistingInput,
    Agenda,
  },
  computed: {
    ...mapState('plan', ['plan']),
    filteredList() {
      return this.plan.agendas.filter((agenda) => !agenda.is_itinerary)
    },
    filteredDays() {
      return this.plan.agendas.filter((agenda) => agenda.is_itinerary)
    },
  },
  mounted() {
    this.fetchPlan({
      planId: 1,
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
    handleAddAgenda({ is_itinerary }) {
      this.addAgenda({
        is_itinerary,
        onSuccess: this.onSuccess,
        onError: this.onError,
      })
    },
    ...mapActions('plan', ['fetchPlan', 'addAgenda']),
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
