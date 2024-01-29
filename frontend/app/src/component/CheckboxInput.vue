<template>
  <div
    :style="{
      ...defaultStyle,
      ...currentStateStyle,
      cursor: currentState === 'disabled' ? 'not-allowed' : 'pointer',
    }"
    @click="saveChanges"
  >
    {{ currentStateLabel }}
  </div>
</template>

<script>
import api from '@/api'
import { CHECKED_STATUS } from '@/constants'

const checkBoxStyle = {
  fontSize: '0',
  transform: 'translate(0px, 4px)',
  width: '15px',
  marginRight: '10px',
  height: '15px',
  backgroundColor: '#fff',
  cursor: 'pointer',
  outline: 'none',
}

export default {
  props: {
    editEndPoint: String,
    itemKey: String,
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
          ...checkBoxStyle,
          backgroundColor: 'red',
        },
        [CHECKED_STATUS.SELECTED]: {
          ...checkBoxStyle,
          backgroundColor: 'green',
        },
        [CHECKED_STATUS.UNSELECTED]: {
          ...checkBoxStyle,
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
        padding: '8px',
        paddingTop: '4px',
        paddingBottom: '4px',
        border: '1px solid #ccc',
        borderRadius: '4px',
        display: 'inline-block',
        fontSize: 'small',
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
    async saveChanges() {
      if (this.currentStateIndex < this.states.length - 1) {
        this.currentStateIndex++
      } else {
        this.currentStateIndex = 0
      }

      try {
        const patchData = {
          [this.itemKey]: this.states[this.currentStateIndex],
        }
        await api.patch(this.editEndPoint, patchData)
      } catch (error) {
        console.error('Error updating data:', error)
      }
    },
  },
}
</script>

<style scoped>
/* Add your default and other styles here */
</style>
