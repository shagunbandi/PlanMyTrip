// agendaActions.js
import api from '@/api'
import apiMessages from '@/constants/apiMessages'

export const addAgenda = async (
  { state, dispatch },
  {
    newAgenda = { title: 'New Agenda' },
    onSuccess = () => {},
    onError = () => {},
  },
) => {
  const itineraryId = state.itinerary.id
  try {
    await api.post(`/api/planner/itinerary/${itineraryId}/agenda/`, newAgenda)
    dispatch('fetchItinerary', { itineraryId })
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
  const itineraryId = state.itinerary.id
  try {
    await api.delete(
      `/api/planner/itinerary/${itineraryId}/agenda/${agendaId}/`,
    )
    dispatch('fetchItinerary', { itineraryId })
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
  const itineraryId = state.itinerary.id
  try {
    const postData = {
      method: direction,
    }
    await api.post(
      `/api/planner/itinerary/${itineraryId}/agenda/${agendaId}/move/`,
      postData,
    )
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.MOVE_AGENDA_SUCCESS)
  } catch (error) {
    onError(apiMessages.MOVE_AGENDA_FAIL)
    console.error('Error moving agenda:', error)
  }
}
