<template>
  <div
    class="quill-container"
    @mouseover="isHovered = true"
    @mouseleave="isHovered = false"
  >
    <QuillEditor
      v-model:content="quillContent"
      contentType="html"
      :options="quillOptions"
      toolbar="essential"
      @blur="handleQuillChange"
      @change="handleQuillChange"
    />
  </div>
</template>

<script>
import api from '@/api'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'

export default {
  components: {
    QuillEditor,
  },
  props: {
    value: [String, Number],
    editEndPoint: String,
    itemKey: String,
    inputType: String,
    placeholder: String,
  },
  data() {
    return {
      quillContent: '',
      quillOptions: {
        // specify Quill options here
        // for example, modules and theme
        modules: {
          // ... (your toolbar and other modules)
        },
        theme: 'snow', // or 'bubble' for a different theme
      },
    }
  },
  watch: {
    value: {
      handler(newVal) {
        // Update quillContent when the value prop changes
        if (newVal !== this.quillContent) {
          console.log('setting')
          this.quillContent = newVal
        }
      },
      immediate: true, // Run the handler immediately to set the initial content
    },
  },
  methods: {
    handleQuillChange(value) {
      this.saveChanges()
    },
    async saveChanges() {
      try {
        const patchData = {
          [this.itemKey]: this.quillContent,
        }
        await api.patch(this.editEndPoint, patchData)
      } catch (error) {
        console.error('Error updating data:', error)
      }
    },
  },
}
</script>

<style>
.quill-container {
  position: relative;
}

.quill-container:hover .ql-toolbar {
  opacity: 1;
  pointer-events: auto;
  display: block;
}

.quill-container .ql-toolbar {
  display: none;
}

.quill-container .ql-container {
  border: 1px solid transparent;
}

.quill-container:hover .ql-container {
  border: 1px solid #ccc;
}
</style>
