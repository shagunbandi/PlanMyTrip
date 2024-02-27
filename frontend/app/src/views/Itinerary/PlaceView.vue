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
        src: linkIcon,
        clickHandler: () =>
          showFieldEditModal('Place Link', 'link', place.link, 'text'),
      },
      {
        type: 'icon',
        src: currencyIcon,
        clickHandler: () =>
          showFieldEditModal('Cost', 'cost', place.cost, 'number'),
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
        <div
          class="green-box"
          v-if="place.cost"
          @click="
            () => showFieldEditModal('Cost', 'cost', place.cost, 'number')
          "
        >
          {{ place.cost }}
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
            console.log(modalKey, this.modalKey)
            handleEditPlaceField(modalKey, value)
          }
        "
      />
    </div>
  </SideActionPannel>
</template>

<script>
import CurrencyIcon from '@/assets/icons/currency-icon.jpg'
import LinkIcon from '@/assets/icons/link-icon.jpg'
import EditorInput from '@/component/EditorInput.vue'
import ModalInput from '@/component/ModalInput.vue'
import SideActionPannel from '@/component/SideActionPannel.vue'
import { mapActions } from 'vuex'

export default {
  props: {
    place: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      linkIcon: LinkIcon,
      currencyIcon: CurrencyIcon,
      editedTitle: this.place.title,
      editedText: this.place.text,
      showModal: false,
      modalTitle: '',
      modalValue: '',
      modalKey: '',
    }
  },
  components: { SideActionPannel, EditorInput, ModalInput },
  methods: {
    onSuccess(message) {
      this.$toast.success(message, { duration: 5000 })
    },
    onError(message) {
      this.$toast.error(message, { duration: 5000 })
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
        contentType: this.place.content_type,
        objectId: this.place.object_id,
        placeId: this.place.id,
        fieldName: fieldName,
        fieldValue: fieldValue,
        onSucces: this.onSuccess,
        onError: this.onError,
      })
    },
    handleMovePlace(direction) {
      this.movePlace({
        contentType: this.place.content_type,
        objectId: this.place.object_id,
        placeId: this.place.id,
        moveDirection: direction,
        onSucces: this.onSuccess,
        onError: this.onError,
      })
    },
    handleRemovePlace() {
      this.removePlace({
        placeId: this.place.id,
        onSucces: this.onSuccess,
        onError: this.onError,
      })
    },
    ...mapActions('itinerary', ['editPlaceField', 'removePlace', 'movePlace']),
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
