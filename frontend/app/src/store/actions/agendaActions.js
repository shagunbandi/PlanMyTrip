// agendaActions.js
import api from '@/api'
import apiMessages from '@/constants/apiMessages'

export const addAgenda = async (
  { state, dispatch },
  { is_itinerary = false, onSuccess = () => {}, onError = () => {} },
) => {
  const planId = state.plan.id
  const newAgenda = {
    is_itinerary,
  }
  try {
    await api.post(`/api/planner/plan/${planId}/agenda/`, newAgenda)
    dispatch('fetchPlan', { planId })
    onSuccess(apiMessages.AGENDA_ADD_SUCCESS)
  } catch (error) {
    onError(apiMessages.AGENDA_ADD_FAIL)
    console.error('Error adding agenda:', error)
  }
}

export const removeAgenda = async (
  { state, dispatch },
  { agendaId, onSuccess = () => {}, onError = () => {} },
) => {
  const planId = state.plan.id
  try {
    await api.delete(`/api/planner/plan/${planId}/agenda/${agendaId}/`)
    dispatch('fetchPlan', { planId })
    onSuccess(apiMessages.AGENDA_REMOVE_SUCCESS)
  } catch (error) {
    onError(apiMessages.AGENDA_REMOVE_FAIL)
    console.error('Error deleting agenda:', error)
  }
}

export const moveAgenda = async (
  { state, dispatch },
  { agendaId, direction, onSuccess = () => {}, onError = () => {} },
) => {
  const planId = state.plan.id
  try {
    const postData = {
      method: direction,
    }
    await api.post(
      `/api/planner/plan/${planId}/agenda/${agendaId}/move/`,
      postData,
    )
    dispatch('fetchPlan', { planId })
    onSuccess(apiMessages.MOVE_AGENDA_SUCCESS)
  } catch (error) {
    onError(apiMessages.MOVE_AGENDA_FAIL)
    console.error('Error moving agenda:', error)
  }
}
