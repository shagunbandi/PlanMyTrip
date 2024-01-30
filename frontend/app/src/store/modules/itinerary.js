// store/modules/itinerary.js
import api from '@/api'
import * as commonDetailActions from '@/store/actions/commonDetailActions'
import * as dayActions from '@/store/actions/dayActions'

const state = {
  itinerary: null,
  loading: false,
  error: null,
}

const mutations = {
  SET_ITINERARY(state, itinerary) {
    state.itinerary = itinerary
    state.loading = false
    state.error = null
  },
  CLEAR_ITINERARY(state) {
    state.itinerary = null
    state.loading = false
    state.error = null
  },
  SET_ERROR(state, error) {
    state.error = error
    state.loading = false
  },
  SET_LOADING(state, loading) {
    state.loading = loading
    state.error = null
  },
}

const actions = {
  async fetchItinerary({ commit }, itineraryId = 1) {
    try {
      commit('SET_LOADING', true)
      const response = await api.get(`/api/itinerary/${itineraryId}/`)
      commit('SET_ITINERARY', response.data)
    } catch (error) {
      console.error('Error fetching itinerary:', error)
      commit('SET_ERROR', error.message || 'Error fetching itinerary')
    }
  },
  ...dayActions,
  ...commonDetailActions,
}

const getters = {
  getCurrentItinerary: (state) => state.itinerary,
  isLoading: (state) => state.loading,
  getError: (state) => state.error,
}

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters,
}
