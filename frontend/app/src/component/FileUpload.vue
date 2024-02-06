<template>
  <div>
    <a
      v-if="displayValue"
      :href="`http://localhost:8000/media/${displayValue}`"
      target="_blank"
      >File: {{ getLastPart(displayValue) }}</a
    >
    <input type="file" ref="fileInput" @change="handleFileChange" />
    <button v-if="!loading" @click="uploadFile" class="btn btn-success">
      Upload
    </button>
    <button v-else class="btn btn-secondary" disabled>Loading...</button>
  </div>
</template>

<script>
import api from '@/api'

export default {
  props: {
    value: [String],
    editEndPoint: String,
    itemKey: String,
  },
  data() {
    return {
      file: null,
      loading: false,
      displayValue: this.value, // Initialize displayValue with the value of the prop
    }
  },
  methods: {
    handleFileChange(event) {
      this.file = event.target.files[0]
    },

    uploadFile() {
      this.loading = true // Set loading state to true before making the API call
      api
        .patch(
          this.editEndPoint,
          { [this.itemKey]: this.file },
          {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          },
        )
        .then((response) => {
          this.displayValue = response.data[this.itemKey]
          this.file = null
          // Assuming you want to clear the file value upon successful upload
          this.$refs.fileInput.value = null
        })
        .catch((error) => {
          console.error('Error uploading file', error)
        })
        .finally(() => {
          this.loading = false // Set loading state back to false after API call completes
        })
    },
    getLastPart(url) {
      if (url) {
        const parts = url.split('/')
        return parts[parts.length - 1]
      }
      return ''
    },
  },
}
</script>
