<template>
  <span>
    <label>{{ title }}</label>
    <ul>
      <li
        v-for="detail in reservationDetails"
        :key="detail.id"
        class="d-flex align-items-start detail"
      >
        <!-- CHECKBOX -->
        <PersistingEnumSelector
          v-if="isFeatureEnabled(reservationKeys.CHECKED_STATUS)"
          :value="detail[reservationKeys.CHECKED_STATUS]"
          :itemKey="reservationKeys.CHECKED_STATUS"
          :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
        />

        <div class="flex-grow-1">
          <!-- NAME -->
          <PersistingInput
            v-if="isFeatureEnabled(reservationKeys.NAME)"
            inputType="input"
            placeholder="Name"
            :itemKey="reservationKeys.NAME"
            :value="detail[reservationKeys.NAME]"
            :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
          />

          <!-- Notes -->
          <span v-if="isFeatureEnabled(reservationKeys.NOTES)" class="notes">
            <PersistingInput
              inputType="textarea"
              placeholder="Notes"
              :itemKey="reservationKeys.NOTES"
              :value="detail[reservationKeys.NOTES]"
              :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
            />
          </span>

          <!-- Reservation Cost -->
          <PersistingInput
            v-if="isFeatureEnabled(reservationKeys.RESERVATION_COST)"
            inputType="number"
            placeholder="Reservation Cost"
            @click="handleClick"
            :itemKey="reservationKeys.RESERVATION_COST"
            :value="detail[reservationKeys.RESERVATION_COST]"
            :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
          />

          <!-- Reservation Link -->
          <PersistingInput
            v-if="isFeatureEnabled(reservationKeys.RESERVATION_LINK)"
            inputType="link"
            placeholder="Reservation Link"
            @click="handleClick"
            :itemKey="reservationKeys.RESERVATION_LINK"
            :value="detail[reservationKeys.RESERVATION_LINK]"
            :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
          />

          <!-- Reservation File -->
          <PersistingInput
            v-if="isFeatureEnabled(reservationKeys.RESERVATION_FILE)"
            inputType="input"
            placeholder="Reservation File"
            :itemKey="reservationKeys.RESERVATION_FILE"
            :value="detail[reservationKeys.RESERVATION_FILE]"
            :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
          />

          <!-- Reservation Time -->
          <span v-if="isFeatureEnabled(reservationKeys.RESERVATION_TIME)">
            <label class="label-light">Reservation Time:&nbsp;</label>
            <PersistingTimeInput
              :value="detail[reservationKeys.RESERVATION_TIME]"
              :itemKey="reservationKeys.RESERVATION_TIME"
              :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
            />
            <br />
          </span>

          <!-- Reservation Status -->
          <span v-if="isFeatureEnabled(reservationKeys.RESERVATION_STATUS)">
            <label class="label-light">Reservation Status:&nbsp;</label>
            <PersistingEnumSelector
              :value="detail[reservationKeys.RESERVATION_STATUS]"
              :itemKey="reservationKeys.RESERVATION_STATUS"
              :states="Object.keys(reservationStatus)"
              :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
            />
            <br />
          </span>

          <!-- Attration Type -->
          <span v-if="isFeatureEnabled(attractionKeys.ATTRACTION_TYPE)">
            <label class="label-light">Attraction Type:&nbsp;</label>
            <PersistingEnumSelector
              :value="detail[attractionKeys.ATTRACTION_TYPE]"
              :itemKey="attractionKeys.ATTRACTION_TYPE"
              :states="Object.keys(attrationType)"
              :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
            />
            <br />
          </span>

          <div class="button-group">
            <button
              class="cross"
              @click="
                removeReservation({
                  dayId: dayId,
                  reservationId: detail.id,
                  reservationName: name,
                })
              "
            >
              X
            </button>
            <button
              class="move-up"
              @click="
                moveReservation({
                  dayId: dayId,
                  reservationId: detail.id,
                  reservationName: name,
                  moveDirection: 'up',
                })
              "
            >
              ↑
            </button>
            <button
              class="move-down"
              @click="
                moveReservation({
                  dayId: dayId,
                  reservationId: detail.id,
                  reservationName: name,
                  moveDirection: 'down',
                })
              "
            >
              ↓
            </button>
          </div>
        </div>
      </li>
      <HoverButton
        buttonText="Add"
        @buttonClick="
          addReservation({
            dayId: dayId,
            newReservation: cleanNewData,
            reservationName: name,
          })
        "
      />
    </ul>
  </span>
</template>

<script>
import HoverButton from '@/component/HoverButton.vue'
import PersistingEnumSelector from '@/component/PersistingEnumSelector.vue'
import PersistingInput from '@/component/PersistingInput.vue'
import PersistingTimeInput from '@/component/PersistingTimeInput.vue'
import {
  ATTRACTION_ENUM,
  ATTRACTION_KEYS,
  RESERVATION_KEYS,
  RESERVATION_STATUS,
} from '@/constants'
import { mapActions } from 'vuex'

export default {
  components: {
    PersistingInput,
    PersistingEnumSelector,
    PersistingTimeInput,
    HoverButton,
  },
  props: {
    newReservationData: Object,
    dayId: Number,
    reservationDetails: Object,
    name: String,
    title: String,
  },
  data() {
    return {
      reservationKeys: RESERVATION_KEYS,
      attractionKeys: ATTRACTION_KEYS,
      reservationStatus: RESERVATION_STATUS,
      attrationType: ATTRACTION_ENUM,
      features: [],
      cleanNewData: {},
    }
  },
  mounted() {
    this.updateFeatures()
    this.cleanNewData = this.generateNewData()
  },
  watch: {
    reservationDetails: {
      handler() {
        this.updateFeatures()
      },
      deep: true,
    },
  },
  computed: {
    isFeatureEnabled() {
      return (featureKey) => this.features.includes(featureKey)
    },
    generateNewData() {
      return () => {
        if (this.newReservationData) {
          return this.newReservationData
        } else {
          return {
            name: `New ${this.title}`,
            notes: '',
          }
        }
      }
    },
  },
  methods: {
    updateFeatures() {
      if (this.reservationDetails.length > 0)
        this.features = Object.keys(this.reservationDetails[0])
    },
    handleClick() {
      console.log('as')
    },
    ...mapActions('itinerary', [
      'fetchItinerary',
      'addReservation',
      'removeReservation',
      'moveReservation',
    ]),
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

.label-light {
  font-weight: normal;
  font-style: normal;
}

/* For Button Group */
.button-group {
  display: none;
}
.detail:hover .button-group {
  opacity: 1;
  display: block;
}

.button-group button {
  background-color: transparent;
  border: none;
  margin-right: 3px;
}

.cross {
  color: red;
}
</style>
