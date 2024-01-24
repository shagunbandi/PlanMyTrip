<template>
  <div
    :style="{
      ...defaultStyle,
      ...currentStateStyle,
      cursor: currentState === 'disabled' ? 'not-allowed' : 'pointer',
    }"
    @click="toggleState"
  >
    {{ currentStateLabel }}
  </div>
</template>

<script>
import { CHECKED_STATUS } from '@/constants'

export default {
  props: {
    value: {
      type: String,
      default: 'default',
    },
    states: {
      type: Array,
      default: () => Object.keys(CHECKED_STATUS),
    },
    styles: {
      type: Object,
      default: () => ({
        [CHECKED_STATUS.CROSSED]: {
          backgroundColor: 'red',
        },
        [CHECKED_STATUS.SELECTED]: {
          backgroundColor: 'green',
        },
        [CHECKED_STATUS.UNSELECTED]: {
          backgroundColor: 'white',
        },
      }),
    },
  },
  data() {
    return {
      currentStateIndex: 0,
    }
  },
  computed: {
    currentState() {
      return this.states[this.currentStateIndex]
    },
    currentStateStyle() {
      return this.styles[this.currentState]
    },
    currentStateLabel() {
      return this.currentState
    },
    defaultStyle() {
      return {
        fontSize: '0',
        transform: 'translate(0px, 4px)',
        width: '15px',
        marginRight: '10px',
        height: '15px',
        backgroundColor: '#fff',
        border: '1px solid #ccc',
        cursor: 'pointer',
        outline: 'none',
      }
    },
  },
  mounted() {
    const initialIndex = this.states.indexOf(this.value)
    if (initialIndex !== -1) {
      this.currentStateIndex = initialIndex
    }
  },
  methods: {
    toggleState() {
      // Update to next state
      if (this.currentStateIndex < this.states.length - 1) {
        this.currentStateIndex++
      } else {
        this.currentStateIndex = 0
      }

      // Emit an event to notify the parent component
      this.$emit('input', this.currentState)
    },
  },
}
</script>

<style scoped>
/* Add your default and other styles here */
</style>
