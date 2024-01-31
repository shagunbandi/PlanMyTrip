<!-- CSSButton.vue -->
<template>
  <div :class="['button-container', extraClasses]">
    <button
      :class="[
        buttonType === buttonTypes.HOVER ? 'hover-button' : '',
        'button',
      ]"
      @click="handleButtonClick"
    >
      <span class="plus-sign">+</span>&nbsp;
      <span class="button-text">{{ buttonText }}</span>
    </button>
  </div>
</template>

<script>
const ButtonTypes = {
  HOVER: 'hover',
  NORMAL: 'normal',
}

export default {
  props: {
    buttonType: {
      type: String,
      required: false,
      default: ButtonTypes.NORMAL,
      validator: (value) => Object.values(ButtonTypes).includes(value),
    },
    buttonText: {
      type: String,
      required: true,
    },
    extraClasses: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      buttonTypes: ButtonTypes,
    }
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
  padding-top: 10px;
  padding-bottom: 10px;
  overflow: hidden; /* Ensure overflow is hidden for transitioning height */
}

.button-container:hover .hover-button {
  opacity: 1;
  height: auto; /* Transition height instead of display */
}

.button {
  background-color: transparent;
  border: none;
  border-radius: 20px;
  background-color: rgb(207, 243, 207);
  padding: 5px;
  font-size: small;
  padding-left: 15px;
  padding-right: 15px;
  opacity: 1; /* Set initial opacity to 1 */
  transition:
    opacity 0.4s ease,
    height 0.4s ease; /* Add height transition */
}

.hover-button {
  opacity: 0;
  height: 0; /* Initially set height to 0 */
  overflow: hidden; /* Hide content when height is 0 */
  transition:
    opacity 0.4s ease,
    height 0.1s ease; /* Add height transition */
}
</style>
