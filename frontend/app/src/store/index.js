import { createStore } from 'vuex'
import itinerary from './modules/itinerary'

export default createStore({
  modules: {
    itinerary,
    // Add more modules as needed
  },
})
