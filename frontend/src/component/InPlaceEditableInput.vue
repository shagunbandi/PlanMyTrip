<template>
  <input
    v-if="inputType === 'input'"
    :id="itemKey"
    class="form-control-plaintext"
    :placeholder="placeholder"
    v-model="editedInput"
    @blur="saveChanges"
  />
  <textarea
    v-else-if="inputType === 'textarea'"
    :id="itemKey"
    class="form-control-plaintext"
    v-model="editedInput"
    :placeholder="placeholder"
    @blur="saveChanges"
    :rows="calculateRows()"
  ></textarea>
</template>

<script>
import api from '@/api'

export default {
  props: {
    value: String,
    editEndPoint: String,
    itemKey: String,
    inputType: String,
    placeholder: String,
  },
  data() {
    return {
      editedInput: this.value,
    }
  },
  methods: {
    async saveChanges() {
      try {
        const patchData = {
          [this.itemKey]: this.editedInput,
        }
        await api.patch(this.editEndPoint, patchData)
      } catch (error) {
        console.error('Error updating data:', error)
      }
    },
    calculateRows() {
      const numberOfLines = this.editedInput?.split('\n').length || 0
      return Math.max(1, numberOfLines)
    },
  },
}
</script>

<style scoped>
.form-control-plaintext {
  margin: 0;
  padding: 0;
  font: inherit;
  font-weight: inherit;
  font-style: inherit;
  color: inherit;
}
</style>
