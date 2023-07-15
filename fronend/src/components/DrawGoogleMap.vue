<!-- https://vue-map.netlify.app/components/map.html -->
<script>
export default {
  name: 'DrawGoogleMap',
  data() {
    return {
      markers: [
        {
          position: {
            lat: 51.093048,
            lng: 6.84212
          }
        }
      ]
    }
  }
}
</script>

<template>
  <GMapMap :center="markers[0].position" :zoom="7" style="width: 100%; height: 400px">
    <GMapMarker
      :key="index"
      v-for="(m, index) in markers"
      :position="m.position"
      :clickable="true"
      :draggable="true"
    />
  </GMapMap>
</template>
