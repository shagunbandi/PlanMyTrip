<!-- TitledTextInput.vue -->

<template>
  <Container
    ><div class="editable-input">
      <p class="title">
        {{ title }}
      </p>
      <p class="content">
        <InPlaceEditableInputVue
          :value="value"
          inputType="textarea"
          :editEndPoint="editEndPoint"
          :itemKey="itemKey"
        />
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
    InPlaceEditableInputVue,
  },
  props: {
    title: String,
    value: String,
    editEndPoint: String,
    itemKey: String,
  },
  data() {
    return {
      editing: false,
      inputValue: this.value,
    }
  },
}
</script>

<style scoped>
.title {
  font-size: 12px;
  font-weight: bold;
}
</style>
