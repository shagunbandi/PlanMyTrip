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

          <!-- Reservation Time -->
          <span v-if="isFeatureEnabled(detailKeys.RESERVATION_TIME)">
            <label class="label-light">Reservation Time:&nbsp;</label>
            <TimeInput
              :value="detail[detailKeys.RESERVATION_TIME]"
              :itemKey="detailKeys.RESERVATION_TIME"
              :editEndPoint="`/${name}/api/${detail.id}/?day_id=${dayId}`"
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
              :editEndPoint="`/${name}/api/${detail.id}/?day_id=${dayId}`"
            />
            <br />
          </span>
          <div class="button-group">
            <button class="cross" @click="removeDetail(detail.id)">X</button>
            <button class="move-up" @click="moveDay(detail.id, 'up')">↑</button>
            <button class="move-down" @click="moveDay(detail.id, 'down')">
              ↓
            </button>
          </div>
        </div>
      </li>
      <HoverButton buttonText="Add" @buttonClick="handleAddDetail" />
    </ul>
  </span>
</template>

<script>
import api from '@/api'

import CheckboxInput from '@/component/CheckboxInput.vue'
import HoverButton from '@/component/HoverButton.vue'
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'
import TimeInput from '@/component/TimeInput.vue'
import { DETAIL_KEYS, RESERVATION_STATUS } from '@/constants'

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
      reservationStatus: RESERVATION_STATUS,
      features: [],
      cleanNewData: {},
    }
  },
  mounted() {
    if (this.details.length > 0) this.features = Object.keys(this.details[0])
    this.cleanNewData = this.generateNewData()
  },
  emits: ['fetchItinerary'],
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
    fetchItinerary() {
      this.$emit('fetchItinerary')
    },
    async handleAddDetail() {
      try {
        await api.post(
          `/${this.name}/api/?day_id=${this.dayId}`,
          this.cleanNewData,
        )
        this.fetchItinerary()
      } catch (error) {
        console.error(`Error adding ${this.name}:`, error)
      }
    },
    async removeDetail(detailId) {
      try {
        await api.delete(`${this.name}/api/${detailId}/?day_id=${this.dayId}`)
        this.fetchItinerary()
      } catch (error) {
        console.error(`Error removing ${this.name}:`, error)
      }
    },
    async moveDetail(dayId, moveDirection) {
      try {
        await api.post(
          `day/${this.itineraryId}/${dayId}/move/${moveDirection}/`,
        )
        this.fetchItinerary()
      } catch (error) {
        console.error('Error moving day:', error)
      }
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
