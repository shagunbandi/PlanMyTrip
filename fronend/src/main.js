import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import VueGoogleMaps from '@fawmi/vue-google-maps'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyCubBAcZzh5D6l5fYq77Gg3TPVRt5o6d2k'
  }
})

app.mount('#app')
