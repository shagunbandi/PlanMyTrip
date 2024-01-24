<template>
  <label for="notes">Notes</label>
  <InPlaceEditableInput
    title="Notes"
    :value="value"
    :editEndPoint="`/itinerary/api/${itineraryId}/`"
    itemKey="notes"
    placeholder="Write some notes here"
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
