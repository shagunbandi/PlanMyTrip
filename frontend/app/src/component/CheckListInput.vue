<template>
  <div>
    <ul class="list-unstyled">
      <li class="d-flex" v-for="(item, key) in checkedItems" :key="key">
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
        <!-- <span class="m-l-3">{{ item.key }}</span> -->
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
</style>
