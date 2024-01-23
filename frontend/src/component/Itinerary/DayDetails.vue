<template>
  <label v-if="details && details.length > 0">{{ detailTitle }}</label>
  <div v-for="detail in details" :key="detail.id">
    <div class="d-flex align-items-start">
      <input class="flex-shrink-0 checkbox" type="checkbox" />
      <div class="flex-grow-1">
        <InPlaceEditableInput
          inputType="input"
          placeholder="Name"
          itemKey="name"
          :value="detail.name"
          :editEndPoint="`/${detailName}/api/${detail.id}/?day_id=${dayId}`"
        />
        <span class="notes">
          <InPlaceEditableInput
            inputType="textarea"
            placeholder="Notes"
            itemKey="notes"
            :value="detail.notes"
            :editEndPoint="`/${detailName}/api/${detail.id}/?day_id=${dayId}`"
          />
        </span>
      </div>
    </div>
  </div>
  <br />
</template>

<script>
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'

export default {
  components: {
    InPlaceEditableInput,
  },
  props: {
    dayId: Number,
    details: Object,
    detailName: String,
    detailTitle: String,
  },
  data() {
    return {}
  },
  //   emits: ['moveDay', 'removeDay'],
  methods: {
    // removeDay(dishId) {
    //   this.$emit('removeDay', dishId)
    // },
    // moveDay(dishId, moveDirection) {
    //   this.$emit('moveDay', dishId, moveDirection)
    // },
  },
}
</script>

<style scoped>
.checkbox {
  margin-top: 5px;
  margin-right: 8px;
}
.notes {
  color: rgb(79, 79, 79);
  font-style: italic;
}
</style>
