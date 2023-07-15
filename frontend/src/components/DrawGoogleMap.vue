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
  mounted() {}
}
</script>

<template>
  <GMapMap :center="markers[0]" :zoom="7" style="width: 100%; height: 400px">
    <GMapPolyline :path="markers" :editable="true" ref="polyline" />
    <GMapMarker
      :zoomOnClick="true"
      :key="index"
      v-for="(m, index) in markers"
      :position="m"
      :label="{ text: (index+1).toString() }"
      :clickable="true"
    />
  </GMapMap>
</template>
