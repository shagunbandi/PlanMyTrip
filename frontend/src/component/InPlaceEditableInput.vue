<template>
  <span v-if="inputType === 'input'">
    <input
      id="editableInput"
      class="form-control-plaintext"
      v-model="editedTitle"
      @blur="saveChanges"
    />
  </span>
  <span v-else-if="inputType === 'textarea'">
    <textarea
      id="editableInput"
      class="form-control-plaintext"
      v-model="editedTitle"
      @blur="saveChanges"
      :rows="calculateRows()"
    ></textarea>
  </span>
</template>

<script>
import api from '../api'

export default {
  props: {
    value: String,
    editEndPoint: String,
    itemKey: String,
    inputType: String,
  },
  data() {
    return {
      editedTitle: this.value,
    }
  },
  methods: {
    async saveChanges() {
      try {
        const patchData = {
          [this.itemKey]: this.editedTitle,
        }
        const response = await api.patch(this.editEndPoint, patchData)
        this.$emit('title-changed', response.data.title)
      } catch (error) {
        console.error('Error updating data:', error)
        window.alert('Error updating data:\n' + error)
      }
    },
    calculateRows() {
      // Calculate the number of lines in the content
      const numberOfLines = this.editedTitle?.split('\n').length || 0

      // Set a minimum number of rows to prevent the text area from being too small
      const minRows = 1

      // Adjust the number of rows based on the content
      return Math.max(minRows, numberOfLines)
    },
  },
}
</script>

<style scoped></style>
