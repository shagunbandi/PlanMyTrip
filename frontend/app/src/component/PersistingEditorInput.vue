<template>
  <div
    :class="{
      'quill-container quill-container-full': editorType == 'full',
      'quill-container quill-container-hover': editorType == 'hover',
      'quill-container quill-container-small': editorType == 'small',
    }"
    @mouseleave="handleQuillChange()"
  >
    <QuillEditor
      v-model:content="quillContent"
      contentType="html"
      :options="quillOptions"
      :placeholder="placeholder"
      @blur="handleQuillChange"
    />
  </div>
</template>

<script>
import api from '@/api'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'

const EditorTypes = {
  HOVER: 'hover',
  SMALL: 'small',
  FULL: 'full',
}

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
    editorType: {
      type: String,
      default: EditorTypes.SMALL,
    },
  },
  data() {
    return {
      quillContentBefore: '',
      quillContent: '',
      quillOptions: {
        modules: {},
        theme: 'snow',
      },
    }
  },
  watch: {
    value: {
      handler(newVal) {
        // Update quillContent when the value prop changes
        if (newVal !== this.quillContent) {
          this.quillContent = newVal
          this.quillContentBefore = newVal
        }
      },
      immediate: true, // Run the handler immediately to set the initial content
    },
  },
  methods: {
    handleQuillChange(value) {
      if (this.quillContent !== this.quillContentBefore) {
        this.saveChanges()
      }
    },
    async saveChanges() {
      try {
        const patchData = {
          [this.itemKey]: this.quillContent,
        }
        await api.patch(this.editEndPoint, patchData)
        this.quillContentBefore = this.quillContent
      } catch (error) {
        console.error('Error updating data:', error)
      }
    },
  },
}
</script>

<style>
.quill-container,
.quill-container-full {
  position: relative;
  margin-top: 5px;
}

/* Toolbar */
.quill-container .ql-toolbar,
.quill-container-full .ql-toolbar {
  height: 0;
  overflow: hidden;
  padding: 0;
  border: 0px solid #ccc;
  border-bottom: 0px;
  transition:
    all 0.4s ease,
    border-bottom 0s ease;
}

.quill-container-hover:hover .ql-toolbar,
.quill-container-full .ql-toolbar {
  pointer-events: auto;
  height: auto;
  overflow: visible;
  z-index: 1;
  padding: 10px;
  border: 1px solid #ccc;
}

/* Editor */
.quill-container .ql-editor,
.quill-container-full .ql-editor {
  padding: 0px;
  font-size: 16px;
}

/* Container */
.quill-container .ql-container,
.quill-container-full .ql-container {
  border: 0px solid #ccc;
  padding: 0;
  transition: all 0.4s ease;
  margin-bottom: 10px;
}

.quill-container-hover:hover .ql-container,
.quill-container-full .ql-container {
  padding: 20px;
  border: 1px solid #ccc;
}
</style>
