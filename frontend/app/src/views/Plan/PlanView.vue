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
        <h4 class="agenda-wise-plan">Plan</h4>
        <button
          class="btn btn-success"
          @click="() => handleAddAgenda({ is_itinerary: false })"
        >
          Add List
        </button>
        <div v-for="agenda in plan.agendas" :key="agenda.id">
          <Agenda :agenda="agenda" />
        </div>
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
  data() {
    return {}
  },
  computed: {
    ...mapState('plan', ['plan']),
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
