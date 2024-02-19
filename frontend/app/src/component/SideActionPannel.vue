<template>
  <div
    ref="dropdown"
    class="side-action-panel"
    @mouseover="showHoverButton = true"
    @mouseleave="showHoverButton = false"
  >
    <slot></slot>
    <div class="button-group" ref="dropdownButton">
      <button @click="toggleDropdown" class="toggle-button btn">▼</button>
      <div v-if="isOpen" class="action-buttons">
        <span v-for="(button, index) in buttons" :key="index">
          <button
            v-if="button.type == 'button' || button.type == null"
            class="btn action-button"
            @click="button.clickHandler"
            :style="button.style"
          >
            {{ button.text }}
          </button>
          <hr v-if="button.type == 'break'" class="m-0 mx-1" />
          <button
            v-if="button.type == 'icon'"
            class="btn action-button"
            @click="button.clickHandler"
            :style="button.style"
          >
            <img :src="button.src" :alt="button.alt" class="icon" />
          </button>
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
    }
  },
  props: {
    buttons: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    toggleDropdown() {
      this.isOpen = !this.isOpen
      if (this.isOpen) {
        document.addEventListener('click', this.closeDropdownOutside)
      } else {
        document.removeEventListener('click', this.closeDropdownOutside)
      }
    },
    closeDropdown() {
      this.isOpen = false
      document.removeEventListener('click', this.closeDropdownOutside)
    },
    closeDropdownOutside(event) {
      if (
        !this.$refs.dropdown?.contains(event.target) &&
        !this.$refs.dropdownButton?.contains(event.target)
      ) {
        this.closeDropdown()
      }
    },
  },
}
</script>

<style scoped>
.side-action-panel {
  position: relative;
}

.button-group {
  position: absolute;
  left: -35px;
  top: 0;
}

.side-action-panel:hover .toggle-button {
  transform: scale(1);
}

.toggle-button {
  animation: all 0.4s linear;
  transform: scale(0);
  color: gray;
  font-size: 10px;
  overflow: hidden;
  height: 30px;
  width: 30px;
  padding: 0px;
  margin: 0px;
}
.toggle-button:hover {
  color: black;
}

/* Action buttons */
.action-buttons {
  padding: 2.5px;
  position: absolute;
  top: 0;
  display: flex;
  width: 30px;
  flex-direction: column;
  z-index: 1;

  border: 1px solid #ccc;
  background-color: white;
  border-radius: 5px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.1);
}

.action-button {
  width: 25px;
  height: 25px;
  padding: 0px;
  margin-top: 2px;
  margin-bottom: 2px;
  border-radius: 5px;
}

.action-button:hover {
  background-color: rgb(224, 224, 224);
}

/* Icon */
.icon {
  width: 17px;
  height: 17px;
}
</style>
