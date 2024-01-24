<template>
  <label v-if="dishes && dishes.length > 0">{{ dishTitle }}</label>
  <ul>
    <li v-for="dish in dishes" :key="dish.id" class="d-flex align-items-start">
      <CheckboxInput
        :value="dish.checked_status"
        @input="updateCheckboxStatus($event, dish.id)"
      />
      <div class="flex-grow-1">
        <InPlaceEditableInput
          inputType="input"
          placeholder="Name"
          itemKey="name"
          :value="dish.name"
          :editEndPoint="`/${dishName}/api/${dish.id}/?day_id=${dayId}`"
        />
        <span class="notes">
          <InPlaceEditableInput
            inputType="textarea"
            placeholder="Notes"
            itemKey="notes"
            :value="dish.notes"
            :editEndPoint="`/${dishName}/api/${dish.id}/?day_id=${dayId}`"
          />
        </span>
      </div>
    </li>
  </ul>
  <br />
</template>

<script>
import api from '@/api'
import CheckboxInput from '@/component/CheckboxInput.vue'
import InPlaceEditableInput from '@/component/InPlaceEditableInput.vue'

export default {
  components: {
    InPlaceEditableInput,
    CheckboxInput,
  },
  props: {
    dayId: Number,
    dishes: Object,
    dishName: String,
    dishTitle: String,
  },
  data() {
    return {}
  },
  emits: ['fetchItinerary'],
  methods: {
    async updateCheckboxStatus(status, dishId) {
      try {
        const patchData = {
          checked_status: status,
        }
        await api.patch(`dish/api/${dishId}/?day_id=${this.dayId}`, patchData)
      } catch (error) {
        console.error('Error updating data:', error)
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
</style>
