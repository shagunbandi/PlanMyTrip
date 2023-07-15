<template>
  <GMapMap>
    <GMapMarker :key="index" v-for="(m, index) in markers" />
  </GMapMap>
</template>
<script>
export default {
  name: 'App',
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
