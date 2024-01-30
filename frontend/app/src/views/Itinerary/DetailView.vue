<template>
  <span>
    <label>{{ title }}</label>
    <ul>
      <li
        v-for="detail in details"
        :key="detail.id"
        class="d-flex align-items-start detail"
      >
        <!-- CHECKBOX -->
        <CheckboxInput
          v-if="isFeatureEnabled(detailKeys.CHECKED_STATUS)"
          :value="detail[detailKeys.CHECKED_STATUS]"
          :itemKey="detailKeys.CHECKED_STATUS"
          :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
        />

        <div class="flex-grow-1">
          <!-- NAME -->
          <InPlaceEditableInput
            v-if="isFeatureEnabled(detailKeys.NAME)"
            inputType="input"
            placeholder="Name"
            :itemKey="detailKeys.NAME"
            :value="detail[detailKeys.NAME]"
            :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
          />

          <!-- Notes -->
          <span v-if="isFeatureEnabled(detailKeys.NOTES)" class="notes">
            <InPlaceEditableInput
              inputType="textarea"
              placeholder="Notes"
              :itemKey="detailKeys.NOTES"
              :value="detail[detailKeys.NOTES]"
              :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
            />
          </span>

          <!-- Reservation Cost -->
          <InPlaceEditableInput
            v-if="isFeatureEnabled(detailKeys.RESERVATION_COST)"
            inputType="number"
            placeholder="Reservation Cost"
            @click="handleClick"
            :itemKey="detailKeys.RESERVATION_COST"
            :value="detail[detailKeys.RESERVATION_COST]"
            :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
          />

          <!-- Reservation Link -->
          <InPlaceEditableInput
            v-if="isFeatureEnabled(detailKeys.RESERVATION_LINK)"
            inputType="link"
            placeholder="Reservation Link"
            @click="handleClick"
            :itemKey="detailKeys.RESERVATION_LINK"
            :value="detail[detailKeys.RESERVATION_LINK]"
            :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
          />

          <!-- Reservation File -->
          <InPlaceEditableInput
            v-if="isFeatureEnabled(detailKeys.RESERVATION_FILE)"
            inputType="input"
            placeholder="Reservation File"
            :itemKey="detailKeys.RESERVATION_FILE"
            :value="detail[detailKeys.RESERVATION_FILE]"
            :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
          />

          <!-- Reservation Time -->
          <span v-if="isFeatureEnabled(detailKeys.RESERVATION_TIME)">
            <label class="label-light">Reservation Time:&nbsp;</label>
            <TimeInput
              :value="detail[detailKeys.RESERVATION_TIME]"
              :itemKey="detailKeys.RESERVATION_TIME"
              :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
            />
            <br />
          </span>

          <!-- Reservation Status -->
          <span v-if="isFeatureEnabled(detailKeys.RESERVATION_STATUS)">
            <label class="label-light">Reservation Status:&nbsp;</label>
            <CheckboxInput
              :value="detail[detailKeys.RESERVATION_STATUS]"
              :itemKey="detailKeys.RESERVATION_STATUS"
              :states="Object.keys(reservationStatus)"
              :editEndPoint="`/api/${name}/${detail.id}/?day_id=${dayId}`"
            />
            <br />
          </span>

          <!-- Attration Type -->
          <span v-if="isFeatureEnabled(attractionKeys.ATTRACTION_TYPE)">
            <label class="label-light">Attraction Type:&nbsp;</label>
            <CheckboxInput
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
                removeDetail({
                  dayId: dayId,
                  detailId: detail.id,
                  detailName: name,
                })
              "
            >
              X
            </button>
            <button
              class="move-up"
              @click="
                moveDetail({
                  dayId: dayId,
                  detailId: detail.id,
                  detailName: name,
                  moveDirection: 'up',
                })
              "
            >
              ↑
            </button>
            <button
              class="move-down"
              @click="
                moveDetail({
                  dayId: dayId,
                  detailId: detail.id,
                  detailName: name,
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
          addDetail({
            dayId: dayId,
            newDetail: cleanNewData,
            detailName: name,
          })
        "
      />
    </ul>
  </span>
</template>

<script>
import CheckboxInput from '@/component/CheckboxInput.vue'
import HoverButton from '@/component/HoverButton.vue'
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'
import TimeInput from '@/component/TimeInput.vue'
import {
  ATTRACTION_ENUM,
  ATTRACTION_KEYS,
  DETAIL_KEYS,
  RESERVATION_STATUS,
} from '@/constants'
import { mapActions } from 'vuex'

export default {
  components: {
    InPlaceEditableInput,
    CheckboxInput,
    TimeInput,
    HoverButton,
  },
  props: {
    newDetailData: Object,
    dayId: Number,
    details: Object,
    name: String,
    title: String,
  },
  data() {
    return {
      detailKeys: DETAIL_KEYS,
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
    details: {
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
        if (this.newDetailData) {
          return this.newDetailData
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
      if (this.details.length > 0) this.features = Object.keys(this.details[0])
    },
    handleClick() {
      console.log('as')
    },
    ...mapActions('itinerary', [
      'fetchItinerary',
      'addDetail',
      'removeDetail',
      'moveDetail',
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
