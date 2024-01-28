<template>
  <input
    class="time-input"
    type="time"
    v-model="selectedTime"
    @blur="saveChanges"
  />
</template>

<script>
import api from '@/api'

export default {
  props: {
    editEndPoint: String,
    itemKey: String,
    value: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      selectedTime: this.value,
    }
  },
  methods: {
    async saveChanges() {
      try {
        const patchData = {
          [this.itemKey]: this.selectedTime,
        }
        await api.patch(this.editEndPoint, patchData)
      } catch (error) {
        console.error('Error updating data:', error)
      }
    },
  },
}
</script>

<style scoped>
.time-input {
  padding: 8px;
  padding-top: 4px;
  padding-bottom: 4px;
  border: 1px solid #ccc;
  border-radius: 4px;
  display: inline-block;
  font-size: small;
}
</style>
