<!-- PlaceInput.vue -->

<template>
  <input
    type="text"
    class="form-control-plaintext font-weight-bold"
    :placeholder="placeholderText"
    v-model="inputValue"
    @blur="handleBlur"
  />
</template>

<script>
export default {
  props: {
    value: String,
    placeholderText: String,
  },
  data() {
    return {
      inputValue: this.value,
    }
  },
  methods: {
    handleBlur() {
      this.$emit('onblur', this.inputValue)
    },
  },
}
</script>

<style scoped>
/* Add any scoped styles if necessary */
</style>
