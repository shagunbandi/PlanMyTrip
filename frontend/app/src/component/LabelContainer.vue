<!-- Container.vue -->

<template>
  <div class="form-group row">
    <label class="col-sm-4 label-light">{{ label }}</label>
    <div class="col-sm-8">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: { label: String },
}
</script>

<style scoped>
.container {
  background-color: white;
}

.label-light {
  font-weight: normal;
  font-style: normal;
  color: rgb(76, 76, 76);
}
</style>
