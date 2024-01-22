<template>
  <span>
    <span v-if="!editing">
      <span v-if="inputType === 'input'"
        ><span @click="startEditing">{{ editedTitle }}</span></span
      >
      <span v-else-if="inputType === 'textarea'">
        <textarea
          @click="startEditing"
          v-model="editedTitle"
          :rows="calculateRows()"
          readonly
        ></textarea>
      </span>
    </span>
    <span v-else>
      <span v-if="inputType === 'input'"
        ><input
          v-model="editedTitle"
          @input="handleInput"
          @keyup.enter="saveChanges"
      /></span>
      <span v-else-if="inputType === 'textarea'">
        <textarea v-model="editedTitle" @input="handleInput" />
      </span>
      &nbsp;
      <button class="green-btn" @click="saveChanges">Save</button>
    </span>
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
      editing: false,
    }
  },
  methods: {
    startEditing() {
      this.editing = true
    },
    handleInput() {
      // Handle input change
    },
    async saveChanges() {
      try {
        const patchData = {
          [this.itemKey]: this.editedTitle,
        }
        const response = await api.patch(this.editEndPoint, patchData)

        // Assuming your API returns the updated data
        this.$emit('title-changed', response.data.title)

        // If your API doesn't return the updated data, you can emit the edited title directly
        // this.$emit('title-changed', this.editedTitle);

        this.editing = false
      } catch (error) {
        console.error('Error updating data:', error)
        // Handle error as needed
      }
    },
    calculateRows() {
      // Calculate the number of lines in the content
      const numberOfLines = this.editedTitle?.split('\n').length || 0

      // Set a minimum number of rows to prevent the text area from being too small
      const minRows = this.editing ? numberOfLines + 4 : 1
      console.log(minRows)

      // Adjust the number of rows based on the content
      return Math.max(minRows, numberOfLines)
    },
  },
}
</script>

<style scoped>
/* Add your styling as needed */
input {
  border-radius: 4px;
  border: none;
  padding: 8px; /* Adjust the padding as needed */
  box-sizing: border-box;
  outline: none; /* Remove default focus outline */
  color: white;
  background-color: rgba(0, 0, 0, 0.3);
  font-size: inherit;
}

textarea {
  width: 100%;
  border-radius: 4px;
  border: none;
  padding: 8px; /* Adjust the padding as needed */
  box-sizing: border-box;
  outline: none; /* Remove default focus outline */
  color: white;
  background-color: rgba(0, 0, 0, 0.3);
  font-size: inherit;
  resize: vertical;
}

textarea[readonly] {
  background-color: transparent;
  font: inherit;
}
</style>
