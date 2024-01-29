<template>
  <label for="scratchpad">ScratchPad</label>
  <InPlaceEditableInput
    title="ScratchPad"
    :value="value"
    :editEndPoint="`/api/itinerary/${itineraryId}/`"
    itemKey="scratchpad"
    placeholder="Write your thoughts here"
    inputType="textarea"
  />
</template>

<script>
import InPlaceEditableInput from '../InPlaceEditableInput.vue'

export default {
  components: {
    InPlaceEditableInput,
  },

  props: {
    value: String,
    itineraryId: Number,
  },
}
</script>
