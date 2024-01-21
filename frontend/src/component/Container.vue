<!-- Container.vue -->

<template>
  <div class="container">
    <slot></slot>
  </div>
</template>

<script>
export default {
  // Component options...
}
</script>

<style scoped>
.container {
  background-color: rgba(0, 0, 0, 0.2); /* Translucent white background */
  border-radius: 10px; /* Rounded edges */
  padding: 10px;
  padding-left: 20px;
  padding-right: 20px;
  margin-bottom: 10px;
}
</style>
