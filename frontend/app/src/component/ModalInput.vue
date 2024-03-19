<template>
  <div v-if="showModal" class="modal">
    <div class="modal-content">
      <h2>{{ title }}</h2>
      <div v-if="inputType == 'timeRange'">
        <label for="startTime">Start Time:</label>
        <input type="time" v-model="inputValue[0]" />

        <label for="endTime">End Time:</label>
        <input type="time" v-model="inputValue[1]" />
      </div>
      <div v-else class="normal-input">
        <input
          :type="inputType"
          v-model="inputValue"
          @keyup.enter="submitForm"
          ref="inputField"
        />
      </div>
      <div class="d-flex">
        <button class="btn btn-danger m-2" @click="closeModal">Close</button>
        <button class="btn btn-success m-2" @click="submitForm">Submit</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    value: Object,
    onSubmit: Function,
    onClose: Function,
    inputType: String,
  },
  data() {
    return {
      showModal: true,
      inputValue: this.value,
    }
  },
  methods: {
    closeModal() {
      this.onClose()
    },
    submitForm() {
      this.onSubmit(this.inputValue)
      this.closeModal()
    },
    focusInputField() {
      this.$refs.inputField?.focus()
    },
  },
  mounted() {
    this.focusInputField()
  },
}
</script>

<style scoped>
.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>
