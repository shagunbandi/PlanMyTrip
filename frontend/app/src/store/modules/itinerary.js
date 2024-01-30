// store/modules/itinerary.js
import api from '@/api'
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
  async addItinerary({ commit }, newItinerary) {
    try {
      commit('SET_LOADING', true)
      const response = await api.post('/api/itinerary/', newItinerary)
      commit('SET_ITINERARY', response.data)
    } catch (error) {
      console.error('Error adding itinerary:', error)
      commit('SET_ERROR', error.message || 'Error adding itinerary')
    }
  },
  async updateItinerary({ commit, state }, updatedItinerary) {
    try {
      commit('SET_LOADING', true)
      const response = await api.put(
        `/api/itinerary/${state.itinerary.id}/`,
        updatedItinerary,
      )
      commit('SET_ITINERARY', response.data)
    } catch (error) {
      console.error('Error updating itinerary:', error)
      commit('SET_ERROR', error.message || 'Error updating itinerary')
    }
  },
  async deleteItinerary({ commit, state }) {
    const itineraryId = state.itinerary.id
    try {
      commit('SET_LOADING', true)
      await api.delete(`/api/itinerary/${itineraryId}/`)
      commit('CLEAR_CURRENT_ITINERARY')
    } catch (error) {
      console.error('Error deleting itinerary:', error)
      commit('SET_ERROR', error.message || 'Error deleting itinerary')
    }
  },
  ...dayActions,
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
