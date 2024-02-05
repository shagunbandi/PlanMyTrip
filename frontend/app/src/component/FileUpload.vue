<!-- FileUpload.vue -->

<template>
  <div>
    <input type="file" ref="fileInput" @change="handleFileChange" />
    <button @click="uploadFile">Upload</button>
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
    }
  },
  methods: {
    handleFileChange(event) {
      this.file = event.target.files[0]
    },

    uploadFile() {
      api
        .patch(
          this.editEndPoint,
          { reservation_file: this.file },
          {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          },
        )
        .then((response) => {
          console.log('File uploaded successfully', response)
        })
        .catch((error) => {
          console.error('Error uploading file', error)
        })
    },
  },
}
</script>
