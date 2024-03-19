<template>
  <SideActionPannel
    extraClass="mt-3"
    :buttons="[
      {
        text: '↑',
        clickHandler: () => handleMovePlace('up'),
      },
      {
        text: '↓',
        clickHandler: () => handleMovePlace('down'),
      },
      {
        text: 'X',
        clickHandler: handleRemovePlace,
        style: { color: 'red' },
      },
      { type: 'break' },
      {
        type: 'icon',
        ficon: 'fa-solid fa-link',
        clickHandler: () => editLink(place),
      },
      {
        type: 'icon',
        ficon: 'fa-solid fa-coins',
        clickHandler: () => editCost(place),
      },
      {
        type: 'icon',
        ficon: 'fa-solid fa-clock',
        clickHandler: () => editTime(place),
      },
    ]"
  >
    <div class="grey-box">
      <input
        type="text"
        class="form-control-plaintext font-weight-bold"
        placeholder="Name of the place"
        v-model="editedTitle"
        @blur="
          () => {
            handleEditPlaceField('title', editedTitle)
          }
        "
      />
      <EditorInput
        placeholder="Put your thoughts here"
        :value="editedText"
        :on-change="
          (value) => {
            handleEditPlaceField('text', value)
          }
        "
      />
      <div class="d-flex">
        <div class="green-box" v-if="place.link">
          <a :href="place.link" target="_blank">{{ place.link }}</a>
        </div>
        <div class="green-box" v-if="place.cost" @click="() => editCost(place)">
          {{ place.cost }}
        </div>
        <div
          class="green-box"
          v-if="place.start_time || place.end_time"
          @click="() => editTime(place)"
        >
          {{ formattedTimeRange }}
        </div>
      </div>

      <ModalInput
        v-if="showModal"
        :title="modalTitle"
        :value="modalValue"
        :inputType="modalType"
        :onClose="
          () => {
            showModal = false
          }
        "
        :onSubmit="
          (value) => {
            handleEditPlaceField(modalKey, value)
          }
        "
      />
    </div>
  </SideActionPannel>
</template>

<script>
import EditorInput from '@/component/EditorInput.vue'
import ModalInput from '@/component/ModalInput.vue'
import SideActionPannel from '@/component/SideActionPannel.vue'
import moment from 'moment'
import { mapActions } from 'vuex'

export default {
  props: {
    place: {
      type: Object,
      required: true,
    },
    agendaId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      editedTitle: this.place.title,
      editedText: this.place.text,
      showModal: false,
      modalTitle: '',
      modalValue: '',
      modalKey: '',
    }
  },
  components: { SideActionPannel, EditorInput, ModalInput },
  computed: {
    formattedTimeRange() {
      const inputFormat = 'HH:mm:ss'
      const outputFormat = 'hh:mm A'
      const start = moment(this.place.start_time, inputFormat).format(
        outputFormat,
      )
      const end = moment(this.place.end_time, inputFormat).format(outputFormat)
      return `${start} - ${end}`
    },
  },
  methods: {
    onSuccess(message) {
      this.$toast.success(message, { duration: 5000 })
    },
    onError(message) {
      this.$toast.error(message, { duration: 5000 })
    },
    editLink(place) {
      this.showFieldEditModal('Place Link', 'link', place.link, 'text')
    },
    editCost(place) {
      this.showFieldEditModal('Cost', 'cost', place.cost, 'number')
    },
    editTime(place) {
      this.showFieldEditModal(
        'Time Range',
        ['start_time', 'end_time'],
        [place.start_time, place.end_time],
        'timeRange',
      )
    },
    showFieldEditModal(modalTitle, modalKey, modalValue, modalType) {
      this.modalTitle = modalTitle
      this.modalValue = modalValue
      this.modalKey = modalKey
      this.modalType = modalType
      this.showModal = true
    },
    handleEditPlaceField(fieldName, fieldValue) {
      this.editPlaceField({
        placeId: this.place.id,
        agendaId: this.agendaId,
        fieldName: fieldName,
        fieldValue: fieldValue,
        onSucces: this.onSuccess,
        onError: this.onError,
      })
    },
    handleMovePlace(method) {
      this.movePlace({
        placeId: this.place.id,
        agendaId: this.agendaId,
        method: method,
        onSucces: this.onSuccess,
        onError: this.onError,
      })
    },
    handleRemovePlace() {
      this.removePlace({
        placeId: this.place.id,
        agendaId: this.agendaId,
        onSucces: this.onSuccess,
        onError: this.onError,
      })
    },
    ...mapActions('plan', ['editPlaceField', 'removePlace', 'movePlace']),
  },
}
</script>

<style scoped>
.d-flex {
  padding: 0px;
}
.green-box {
  background-color: green;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  max-width: 20ch;
  color: white;
  width: fit-content;
  padding: 16px;
  padding-top: 4px;
  padding-bottom: 4px;
  cursor: pointer;
  margin-right: 4px;
}

.green-box a {
  all: unset;
}
</style>
