<!-- Container.vue -->

<template>
  <div :class="['container', 'position-relative', extraClasses]">
    <slot></slot>
  </div>
</template>

<script>
export default {
  props: { extraClasses: String },
}
</script>

<style scoped>
.container {
  background-color: white;
}

.left-border {
  border-left: grey 5px solid;
}
</style>
