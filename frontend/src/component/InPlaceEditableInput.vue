<template>
  <div>
    <span v-if="inputType === 'input'" class="d-flex">
      <a
        v-if="isLink"
        :href="editedInput"
        target="_blank"
        rel="noopener noreferrer"
        >open</a
      >&nbsp;
      <input
        :id="itemKey"
        class="form-control-plaintext"
        :placeholder="placeholder"
        v-model="editedInput"
        @blur="saveChanges"
      />
    </span>

    <textarea
      v-if="inputType === 'textarea'"
      :id="itemKey"
      class="form-control-plaintext"
      v-model="editedInput"
      :placeholder="placeholder"
      @blur="saveChanges"
      :rows="calculateRows()"
    ></textarea>
  </div>
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
  computed: {
    isLink() {
      // Add your condition to determine if it should be displayed as a link
      return this.isValidLink(this.editedInput)
    },
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
    isValidLink(link) {
      // Add your link validation logic here
      // For simplicity, let's assume a link starting with "http://" or "https://"
      return link && (link.startsWith('http://') || link.startsWith('https://'))
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

/* Add your link styling as needed */
a {
  text-decoration: underline;
  color: blue;
}
</style>
