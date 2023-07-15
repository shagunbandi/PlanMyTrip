<script>
import axios from 'axios'
import ItineraryAtom from '../components/ItineraryAtom.vue'

export default {
  name: 'MainView',
  data() {
    return {
      items: []
    }
  },
  components: {
    ItineraryAtom
  },
  methods: {
    getItems() {
      axios
        .post('http://localhost:5000/', {
          is_prompt: false,
          country: 'India',
          number_of_days: '2'
        })
        .then((response) => {
          this.items = response?.data?.response?.content
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  mounted() {
    this.getItems()
  }
}
</script>

<template>
  <div class="compound">
    <ul>
      <ItineraryAtom
        v-for="(item, index) in this.items"
        :key="index"
        :previous_item="index === 0 ? None : this.items[index - 1]"
        :city="item.gpt_city"
        :category="item.category"
        :name="item.gpt_name"
        :location_name="item.details.name"
        :rating="item.details.rating"
        :user_ratings_total="item.details.user_ratings_total"
        :time="item.time"
        :place_id="item.details.place_id"
      />
    </ul>
  </div>
</template>
