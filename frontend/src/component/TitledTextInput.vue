<!-- TitledTextInput.vue -->

<template>
  <Container
    ><div class="editable-input">
      <p class="title">
        {{ title }}
      </p>
      <p class="content">
        <InPlaceEditableInputVue :value="value" inputType="textarea" />
      </p>
    </div>
  </Container>
</template>

<script>
import Container from './Container.vue'
import InPlaceEditableInputVue from './InPlaceEditableInput.vue'

export default {
  components: {
    Container,

    InPlaceEditableInputVue
  },

  props: {
    title: String,
    value: String
  },
  data() {
    return {
      editing: false,
      inputValue: this.value
    }
  },
  methods: {
    toggleEditMode() {
      if (this.editing) {
        // Save logic (e.g., update backend, if needed)
        // Here, we are just toggling back to read-only mode
        this.editing = false
      } else {
        // Switch to edit mode
        this.editing = true
      }
    },
    handleInput() {
      // Handle input changes, if needed
    }
  }
}
</script>

<style scoped>
.title {
  font-size: 12px;
  font-weight: bold;
}

</style>
