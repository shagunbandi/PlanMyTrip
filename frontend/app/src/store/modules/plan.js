// store/modules/plan.js
import api from '@/api'
import apiMessages from '@/constants/apiMessages'
import * as agendaActions from '@/store/actions/agendaActions'
import * as placeActions from '@/store/actions/placeActions'

const state = {
  plan: null,
  loading: false,
  error: null,
}

const mutations = {
  SET_PLAN(state, plan) {
    state.plan = plan
    state.loading = false
    state.error = null
  },
  CLEAR_PLAN(state) {
    state.plan = null
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
  async fetchPlan(
    { commit },
    { planId, onError = () => {}, onSuccess = () => {} },
  ) {
    try {
      commit('SET_LOADING', true)
      const response = await api.get(`/api/planner/plan/${planId}/`)
      commit('SET_PLAN', response.data)
      onSuccess(apiMessages.PLAN_FETCH_SUCCESS)
    } catch (error) {
      onError(apiMessages.PLAN_FETCH_FAIL)
      commit('SET_PLAN', null)
      commit('SET_ERROR', error.message || 'Error fetching plan')
    }
  },
  ...agendaActions,
  ...placeActions,
}

const getters = {
  getCurrentPlan: (state) => state.plan,
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
