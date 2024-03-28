<template>
  <div>
    <ul class="list-unstyled">
      <li
        class="d-flex hoverable"
        v-for="(item, key) in checkedItems"
        :key="key"
      >
        <input
          type="checkbox"
          :checked="item.value"
          :onclick="() => handleCheckboxClicked(key)"
        />
        <input
          type="text"
          class="form-control-plaintext m-l-5"
          :value="item.key"
          @change="(event) => onTextChangeHandler(key, event.target.value)"
        />
        <i
          v-if="key > 0"
          class="fa-solid fa-arrow-up cursor-pointer"
          @click="handleUpClicked(key)"
        />
        <i
          v-if="key < this.checkedItems.length - 1"
          class="fa-solid fa-arrow-down cursor-pointer m-l-10"
          @click="handleDownClicked(key)"
        />
        <i
          class="fa-solid fa-xmark cursor-pointer m-l-10 cross-mark"
          @click="handleRemovedClicked(key)"
        />
      </li>
      <li :onclick="() => addCheckbox()">
        <input type="checkbox" :disabled="true" />
        <span class="m-l-3 add-another-item">Add another item</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      required: true,
    },
    onChange: Function,
  },
  data() {
    let parsedData = []
    try {
      parsedData = JSON.parse(this.value)
    } catch (error) {
      console.error('Error parsing JSON:', error)
    }
    return {
      checkedItems: parsedData,
    }
  },
  methods: {
    addCheckbox() {
      this.checkedItems.push({
        key: 'New Item',
        value: false,
      })
    },
    handleUpClicked(key) {
      if (key > 0) {
        const temp = this.checkedItems[key]
        this.checkedItems.splice(key, 1)
        this.checkedItems.splice(key - 1, 0, temp)
        this.updateJson()
      }
    },
    handleDownClicked(key) {
      if (key < this.checkedItems.length - 1) {
        const temp = this.checkedItems[key]
        this.checkedItems.splice(key, 1)
        this.checkedItems.splice(key + 1, 0, temp)
        this.updateJson()
      }
    },
    handleRemovedClicked(key) {
      this.checkedItems.splice(key, 1)
      this.updateJson()
    },
    onTextChangeHandler(position, value) {
      this.checkedItems[position].key = value
      this.updateJson()
    },
    handleCheckboxClicked(position) {
      this.checkedItems[position].value = !this.checkedItems[position].value
      this.updateJson()
    },
    updateJson() {
      this.onChange(JSON.stringify(this.checkedItems))
    },
  },
}
</script>

<style scoped>
.add-another-item {
  font-style: italic;
  color: grey;
}
.form-control-plaintext {
  margin-top: 0;
  margin-bottom: 0;
  padding: 0;
}
.cross-mark {
  color: red;
  cursor: pointer;
}
.hoverable i {
  display: none; /* Hide the icons by default */
}

.hoverable:hover i {
  display: inline-block; /* Show the icons when the li is hovered */
}
</style>
