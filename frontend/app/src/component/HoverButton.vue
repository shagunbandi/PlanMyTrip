<!-- CSSButton.vue -->
<template>
  <div class="button-container">
    <button class="button" @click="handleButtonClick">
      <span class="plus-sign">+</span>&nbsp;
      <span class="button-text">{{ buttonText }}</span>
    </button>
  </div>
</template>

<script>
export default {
  props: {
    buttonType: {
      type: String,
      required: false,
      default: 'add',
    },
    buttonText: {
      type: String,
      required: true,
    },
  },
  emits: ['buttonClick'],
  methods: {
    handleButtonClick() {
      this.$emit('buttonClick')
    },
  },
}
</script>

<style scoped>
.button-container {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 0px;
}

.button-container:hover {
  height: auto;
  padding-top: 10px;
  padding-bottom: 10px;
}
.button-container:hover .button {
  opacity: 1;
}

.button {
  opacity: 0;
  background-color: transparent;
  border: none;
  display: inline-block;
  border-radius: 20px;
  background-color: rgb(207, 243, 207);
  padding: 5px;
  font-size: small;
  padding-left: 15px;
  padding-right: 15px;
  transition: opacity 0.1s ease;
}
</style>
