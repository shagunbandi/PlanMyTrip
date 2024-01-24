<!-- components/ThreeStateCheckbox.vue -->

<template>
  <button
    :class="{
      selected: isSelected,
      unselected: isUnselected,
      crossed: isCrossed,
    }"
    class="checkbox"
    @click="toggleState"
  >
    <span v-if="isSelected">✔</span>
    <span v-else-if="isUnselected"></span>
    <span v-else-if="isCrossed">✘</span>
  </button>
</template>

<script>
import { CHECK_STATUS_ENUM } from '@/constants'

export default {
  props: {
    value: {
      type: String,
      default: CHECK_STATUS_ENUM.UNSELECTED,
      enum: CHECK_STATUS_ENUM,
    },
    extraClass: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      isSelected: true,
      isUnselected: false,
      isCrossed: false,
    }
  },
  mounted() {
    this.isUnselected = false
    this.isSelected = false
    this.isCrossed = false
    if (this.value === CHECK_STATUS_ENUM.UNSELECTED) {
      this.isUnselected = true
    } else if (this.value === CHECK_STATUS_ENUM.SELECTED) {
      this.isSelected = true
    } else {
      this.isCrossed = true
    }
  },
  emits: ['input'],
  methods: {
    toggleState() {
      if (this.isUnselected) {
        this.isUnselected = false
        this.isSelected = true
        this.isCrossed = false
        this.$emit('input', CHECK_STATUS_ENUM.SELECTED)
      } else if (this.isSelected) {
        this.isUnselected = false
        this.isSelected = false
        this.isCrossed = true
        this.$emit('input', CHECK_STATUS_ENUM.CROSSED)
      } else {
        this.isUnselected = true
        this.isSelected = false
        this.isCrossed = false
        this.$emit('input', CHECK_STATUS_ENUM.UNSELECTED)
      }
    },
  },
}
</script>

<style scoped>
.checkbox {
  width: 15px;
  height: 15px;
  background-color: #fff;
  border: 1px solid #ccc;
  cursor: pointer;
  outline: none;
}

.checkbox.selected {
  background-color: #66bb6a; /* green color for selected state */
}

.checkbox.unselected {
  /* Styles for unselected state (empty) */
}

.checkbox.crossed {
  background-color: #ef5350; /* red color for crossed state */
}

.checkbox span {
  font-size: 18px;
  color: #fff;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 0;
}

.checkbox.selected span,
.checkbox.crossed span {
  opacity: 1;
}
</style>
