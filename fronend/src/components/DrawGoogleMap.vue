<!-- https://vue-map.netlify.app/components/map.html -->
<script>
export default {
  name: 'DrawGoogleMap',
  data() {
    return {}
  },
  props: {
    markers: Array
  },
  mounted() {
    console.log(this.markers)
  }
}
</script>

<template>
  <GMapMap :center="markers[0]" :zoom="7" style="width: 100%; height: 400px">
    <GMapMarker
      :key="index"
      v-for="(m, index) in markers"
      :position="m"
      :clickable="true"
      :draggable="true"
    />
  </GMapMap>
</template>
