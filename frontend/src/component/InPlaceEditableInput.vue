<template>
  <span>
    <span v-if="!editing">
      <span @click="startEditing">{{ editedTitle }}</span>
    </span>
    <span v-else>
      <span v-if="inputType === 'input'"><input v-model="editedTitle" @input="handleInput" /></span>
      <span v-else-if="inputType === 'textarea'">
        <textarea v-model="editedTitle" @input="handleInput" />
      </span>
      &nbsp;
      <button class="green-button" @click="saveChanges">Save</button>
    </span>
  </span>
</template>

<script>
export default {
  props: {
    value: String,
    inputType: String
  },
  data() {
    return {
      editedTitle: this.value,
      editing: false
    }
  },
  methods: {
    startEditing() {
      this.editing = true
    },
    handleInput() {
      // Handle input changes if needed
    },
    saveChanges() {
      this.editing = false
      this.$emit('title-changed', this.editedTitle)
    }
  }
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
</style>
