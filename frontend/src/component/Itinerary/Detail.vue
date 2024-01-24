<template>
  <label v-if="details && details.length > 0">{{ title }}</label>
  <ul>
    <li
      v-for="detail in details"
      :key="detail.id"
      class="d-flex align-items-start"
    >
      <!-- CHECKBOX -->
      <CheckboxInput
        v-if="isFeatureEnabled(detailKeys.CHECKED_STATUS)"
        :value="detail[detailKeys.CHECKED_STATUS]"
        :itemKey="detailKeys.CHECKED_STATUS"
        :editEndPoint="`/${name}/api/${detail.id}/?day_id=${dayId}`"
      />

      <div class="flex-grow-1">
        <!-- NAME -->
        <InPlaceEditableInput
          v-if="isFeatureEnabled(detailKeys.NAME)"
          inputType="input"
          placeholder="Name"
          :itemKey="detailKeys.NAME"
          :value="detail[detailKeys.NAME]"
          :editEndPoint="`/${name}/api/${detail.id}/?day_id=${dayId}`"
        />

        <!-- Notes -->
        <span v-if="isFeatureEnabled(detailKeys.NOTES)" class="notes">
          <InPlaceEditableInput
            inputType="textarea"
            placeholder="Notes"
            :itemKey="detailKeys.NOTES"
            :value="detail[detailKeys.NOTES]"
            :editEndPoint="`/${name}/api/${detail.id}/?day_id=${dayId}`"
          />
        </span>

        <!-- Reservation Link -->
        <InPlaceEditableInput
          v-if="isFeatureEnabled(detailKeys.RESERVATION_LINK)"
          inputType="input"
          placeholder="Reservation Link"
          :itemKey="detailKeys.RESERVATION_LINK"
          :value="detail[detailKeys.RESERVATION_LINK]"
          :editEndPoint="`/${name}/api/${detail.id}/?day_id=${dayId}`"
        />

        <!-- Reservation File -->
        <InPlaceEditableInput
          v-if="isFeatureEnabled(detailKeys.RESERVATION_FILE)"
          inputType="input"
          placeholder="Reservation File"
          :itemKey="detailKeys.RESERVATION_FILE"
          :value="detail[detailKeys.RESERVATION_FILE]"
          :editEndPoint="`/${name}/api/${detail.id}/?day_id=${dayId}`"
        />

        <!-- Reservation Status -->
        <span v-if="isFeatureEnabled(detailKeys.RESERVATION_STATUS)">
          <label class="reservation-status">Reservation Status:&nbsp;</label>
          <CheckboxInput
            :value="detail[detailKeys.RESERVATION_STATUS]"
            :itemKey="detailKeys.RESERVATION_STATUS"
            :states="Object.keys(reservationStatus)"
            :editEndPoint="`/${name}/api/${detail.id}/?day_id=${dayId}`"
          />
        </span>
      </div>
    </li>
  </ul>
  <br />
</template>

<script>
import CheckboxInput from '@/component/CheckboxInput.vue'
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'
import { DETAIL_KEYS, RESERVATION_STATUS } from '@/constants'

export default {
  components: {
    InPlaceEditableInput,
    CheckboxInput,
  },
  props: {
    dayId: Number,
    details: Object,
    name: String,
    title: String,
  },
  data() {
    return {
      detailKeys: DETAIL_KEYS,
      reservationStatus: RESERVATION_STATUS,
      features: [],
    }
  },
  mounted() {
    if (this.details.length > 0) this.features = Object.keys(this.details[0])
  },
  emits: ['fetchItinerary'],
  computed: {
    isFeatureEnabled() {
      return (featureKey) => this.features.includes(featureKey)
    },
  },
}
</script>

<style scoped>
ul {
  padding-left: 0;
}
.checkbox {
  margin-top: 5px;
  margin-right: 8px;
}
.notes {
  color: rgb(79, 79, 79);
  font-style: italic;
}

.reservation-status {
  font-weight: normal;
  font-style: normal;
}
</style>
