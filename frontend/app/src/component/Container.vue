<!-- Container.vue -->

<template>
  <div :class="['container', 'position-relative', extraClasses]">
    <span
      v-if="collapsable && isCollapsed"
      @click="toggleCollapse"
      class="clickable"
      >Read More</span
    >
    <slot v-if="!collapsable || !isCollapsed"></slot>
    <span
      v-if="collapsable && !isCollapsed"
      @click="toggleCollapse"
      class="clickable"
      >Collapse</span
    >
  </div>
</template>

<script>
export default {
  props: {
    extraClasses: String,
    collapsable: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data() {
    return {
      isCollapsed: true,
    }
  },
  methods: {
    toggleCollapse() {
      this.isCollapsed = !this.isCollapsed
    },
  },
}
</script>

<style scoped>
.container {
  background-color: white;
}

.left-border {
  border-left: grey 4px solid;
}
</style>
