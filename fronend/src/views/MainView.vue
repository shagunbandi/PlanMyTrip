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
          console.log(response?.data?.response?.content)
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
        :city="item.major_city"
        :category="item.category"
        :name="item.name"
      />
    </ul>
  </div>
</template>
