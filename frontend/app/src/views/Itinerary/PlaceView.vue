<template>
  <SideActionPannel
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
        clickHandler: handleAddPlace,
      },
      {
        type: 'icon',
        src: currencyIcon,
        clickHandler: handleAddPlace,
      },
    ]"
  >
    <div class="card w-100 mb-2">
      <div class="card-body">
        <h5 class="card-title">
          <input
            type="text"
            class="form-control-plaintext"
            placeholder="Name of the place"
            v-model="editedTitle"
            @blur="handleEditPlaceTitle"
          />
        </h5>
      </div>
    </div>
  </SideActionPannel>
</template>

<script>
import CurrencyIcon from '@/assets/icons/currency-icon.jpg'
import LinkIcon from '@/assets/icons/link-icon.jpg'
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
    }
  },
  components: { SideActionPannel },
  methods: {
    onSuccess(message) {
      this.$toast.success(message, { duration: 5000 })
    },
    onError(message) {
      this.$toast.error(message, { duration: 5000 })
    },
    handleEditPlaceTitle() {
      this.editPlaceTitle({
        contentType: this.place.content_type,
        objectId: this.place.object_id,
        placeId: this.place.id,
        placeName: this.editedTitle,
        onSucces: this.onSuccess,
        onError: this.onError,
      })
    },
    handleMovePlace() {},
    handleRemovePlace() {
      this.removePlace({
        placeId: this.place.id,
        onSucces: this.onSuccess,
        onError: this.onError,
      })
    },
    handleAddPlace() {},
    ...mapActions('itinerary', ['editPlaceTitle', 'removePlace', 'movePlace']),
  },
}
</script>

<style scoped></style>
