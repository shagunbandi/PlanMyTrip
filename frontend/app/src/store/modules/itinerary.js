// store/modules/itinerary.js
import api from '@/api'
import apiMessages from '@/constants/apiMessages'
import * as agendaActions from '@/store/actions/agendaActions'
import * as placeActions from '@/store/actions/placeActions'

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
  async fetchItinerary(
    { commit },
    { itineraryId, onError = () => {}, onSuccess = () => {} },
  ) {
    try {
      commit('SET_LOADING', true)
      const response = await api.get(`/api/planner/itinerary/${itineraryId}/`)
      commit('SET_ITINERARY', response.data)
      onSuccess(apiMessages.ITINERARY_FETCH_SUCCESS)
    } catch (error) {
      onError(apiMessages.ITINERARY_FETCH_FAIL)
      commit('SET_ITINERARY', null)
      commit('SET_ERROR', error.message || 'Error fetching itinerary')
    }
  },
  ...agendaActions,
  ...placeActions,
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
