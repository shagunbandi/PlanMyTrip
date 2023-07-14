<script setup>
import ItineraryAtom from '../components/ItineraryAtom.vue'

const data = {
  content: [
    {
      category: 'Adventure',
      day_number: '1st day',
      major_city: 'Paro',
      name: "Tiger's Nest",
      time: '9am'
    },
    {
      category: 'Historic',
      day_number: '1st day',
      major_city: 'Agra',
      name: 'Taj Mahal',
      time: '3pm'
    },
    {
      category: 'Adventure',
      day_number: '2nd day',
      major_city: 'Goa',
      name: 'Dudhsagar Falls',
      time: '9am'
    },
    {
      category: 'Historic',
      day_number: '2nd day',
      major_city: 'Jodhpur',
      name: 'Mehrangarh Fort',
      time: '3pm'
    },
    {
      category: 'Cultural',
      day_number: '2nd day',
      major_city: 'Kochi',
      name: 'Kathakali Performance',
      time: '6pm'
    }
  ]
}
</script>

<template>
  <div class="compound">
    <ul>
      <ItineraryAtom
        v-for="(item, index) in data.content"
        :key="index"
        :city="item.major_city"
        :category="item.category"
        :name="item.name"
      />
    </ul>
  </div>
</template>

<style scoped></style>
