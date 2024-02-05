<template>
  <span>
    <label>{{ title }}</label>
    <ul>
      <div v-for="detail in reservationDetails" :key="detail.id" class="detail">
        <li class="d-flex align-items-start">
          <!-- CHECKBOX -->
          <PersistingEnumSelector
            v-if="isFeatureEnabled(reservationKeys.CHECKED_STATUS)"
            :value="detail[reservationKeys.CHECKED_STATUS]"
            :itemKey="reservationKeys.CHECKED_STATUS"
            :editEndPoint="`/api/itinerary/${itinerary.id}/day/${dayId}/${name}/${detail.id}/`"
          />

          <div class="flex-grow-1">
            <!-- NAME -->
            <PersistingInput
              v-if="isFeatureEnabled(reservationKeys.NAME)"
              inputType="input"
              placeholder="Name"
              :itemKey="reservationKeys.NAME"
              :value="detail[reservationKeys.NAME]"
              :editEndPoint="`/api/itinerary/${itinerary.id}/day/${dayId}/${name}/${detail.id}/`"
            />

            <!-- Notes -->
            <span v-if="isFeatureEnabled(reservationKeys.NOTES)" class="notes">
              <PersistingEditorInput
                placeholder="Notes"
                :itemKey="reservationKeys.NOTES"
                :value="detail[reservationKeys.NOTES]"
                :editEndPoint="`/api/itinerary/${itinerary.id}/day/${dayId}/${name}/${detail.id}/`"
              />
            </span>

            <Container
              extraClasses="left-border"
              v-if="numberOfFeaturesEnabled() >= 1"
              :collapsable="numberOfFeaturesEnabled() >= 2"
            >
              <!-- Reservation Cost -->
              <LabelContainer
                v-if="isFeatureEnabled(reservationKeys.RESERVATION_COST)"
                label="Reservation Cost"
              >
                <PersistingInput
                  id="reservation-cost"
                  inputType="number"
                  placeholder="How much does it cost?"
                  @click="handleClick"
                  :itemKey="reservationKeys.RESERVATION_COST"
                  :value="detail[reservationKeys.RESERVATION_COST]"
                  :editEndPoint="`/api/itinerary/${itinerary.id}/day/${dayId}/${name}/${detail.id}/`"
                />
              </LabelContainer>

              <!-- Reservation Link -->
              <LabelContainer
                v-if="isFeatureEnabled(reservationKeys.RESERVATION_LINK)"
                label="Reservation Link"
              >
                <PersistingInput
                  inputType="link"
                  placeholder="Link to your reservation"
                  @click="handleClick"
                  :itemKey="reservationKeys.RESERVATION_LINK"
                  :value="detail[reservationKeys.RESERVATION_LINK]"
                  :editEndPoint="`/api/itinerary/${itinerary.id}/day/${dayId}/${name}/${detail.id}/`"
                />
              </LabelContainer>

              <!-- Reservation File -->
              <LabelContainer
                v-if="isFeatureEnabled(reservationKeys.RESERVATION_FILE)"
                label="Reservation File"
              >
                <FileUpload
                  inputType="input"
                  :itemKey="reservationKeys.RESERVATION_FILE"
                  :value="detail[reservationKeys.RESERVATION_FILE]"
                  :editEndPoint="`/api/itinerary/${itinerary.id}/day/${dayId}/${name}/${detail.id}/`"
                />
              </LabelContainer>

              <!-- Reservation Time -->
              <LabelContainer
                v-if="isFeatureEnabled(reservationKeys.RESERVATION_TIME)"
                label="Reservation Time"
              >
                <PersistingTimeInput
                  :value="detail[reservationKeys.RESERVATION_TIME]"
                  :itemKey="reservationKeys.RESERVATION_TIME"
                  :editEndPoint="`/api/itinerary/${itinerary.id}/day/${dayId}/${name}/${detail.id}/`"
                />
              </LabelContainer>

              <!-- Reservation Status -->
              <LabelContainer
                v-if="isFeatureEnabled(reservationKeys.RESERVATION_STATUS)"
                label="Reservation Status"
              >
                <PersistingEnumSelector
                  :value="detail[reservationKeys.RESERVATION_STATUS]"
                  :itemKey="reservationKeys.RESERVATION_STATUS"
                  :states="Object.keys(reservationStatus)"
                  :editEndPoint="`/api/itinerary/${itinerary.id}/day/${dayId}/${name}/${detail.id}/`"
                />
              </LabelContainer>

              <!-- Attration Type -->
              <LabelContainer
                v-if="isFeatureEnabled(attractionKeys.ATTRACTION_TYPE)"
                label="Attraction Type"
              >
                <PersistingEnumSelector
                  :value="detail[attractionKeys.ATTRACTION_TYPE]"
                  :itemKey="attractionKeys.ATTRACTION_TYPE"
                  :states="Object.keys(attrationType)"
                  :editEndPoint="`/api/itinerary/${itinerary.id}/day/${dayId}/${name}/${detail.id}/`"
                />
              </LabelContainer>
            </Container>
          </div>
        </li>
        <div class="button-group pt-1 pb-1">
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
      <ButtonPro
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
import ButtonPro from '@/component/ButtonPro.vue'
import Container from '@/component/Container.vue'
import FileUpload from '@/component/FileUpload.vue'
import LabelContainer from '@/component/LabelContainer.vue'
import PersistingEditorInput from '@/component/PersistingEditorInput.vue'
import PersistingEnumSelector from '@/component/PersistingEnumSelector.vue'
import PersistingInput from '@/component/PersistingInput.vue'
import PersistingTimeInput from '@/component/PersistingTimeInput.vue'
import {
  ATTRACTION_ENUM,
  ATTRACTION_KEYS,
  RESERVATION_KEYS,
  RESERVATION_STATUS,
} from '@/constants'
import { mapActions, mapState } from 'vuex'

export default {
  components: {
    PersistingInput,
    LabelContainer,
    PersistingEnumSelector,
    PersistingTimeInput,
    ButtonPro,
    Container,
    PersistingEditorInput,
    FileUpload,
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
    numberOfFeaturesEnabled() {
      return () => {
        const enabledFeatures = [
          this.isFeatureEnabled(this.reservationKeys.RESERVATION_COST),
          this.isFeatureEnabled(this.reservationKeys.RESERVATION_LINK),
          this.isFeatureEnabled(this.reservationKeys.RESERVATION_FILE),
          this.isFeatureEnabled(this.reservationKeys.RESERVATION_TIME),
          this.isFeatureEnabled(this.reservationKeys.RESERVATION_STATUS),
          this.isFeatureEnabled(this.attractionKeys.ATTRACTION_TYPE),
        ]

        return enabledFeatures.filter(Boolean).length
      }
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
    ...mapState('itinerary', ['itinerary']),
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

/* For Button Group */
.button-group {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s ease;
}

.detail:hover .button-group {
  max-height: 200px; /* Set a maximum height when hovering */
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
