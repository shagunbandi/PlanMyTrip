import { createStore } from 'vuex'
import plan from './modules/plan'

export default createStore({
  modules: {
    plan,
    // Add more modules as needed
  },
})
