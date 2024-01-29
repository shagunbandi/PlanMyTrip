<template>
  <label for="notes">Notes</label>
  <InPlaceEditableInput
    title="Notes"
    :value="value"
    :editEndPoint="`/api/itinerary/${itineraryId}/`"
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
