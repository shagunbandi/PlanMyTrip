// dayActions.js
import api from '@/api'
import apiMessages from '@/constants/apiMessages'

export const addDay = async (
  { state, dispatch },
  { newDay = { title: 'New Day' }, onSuccess = () => {}, onError = () => {} },
) => {
  const itineraryId = state.itinerary.id
  try {
    await api.post(`/api/planner/itinerary/${itineraryId}/day/`, newDay)
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.DAY_ADD_SUCCESS)
  } catch (error) {
    onError(apiMessages.DAY_ADD_FAIL)
    console.error('Error adding day:', error)
  }
}

export const removeDay = async (
  { state, dispatch },
  { dayId, onSuccess = () => {}, onError = () => {} },
) => {
  const itineraryId = state.itinerary.id
  try {
    await api.delete(`/api/planner/itinerary/${itineraryId}/day/${dayId}/`)
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.DAY_REMOVE_SUCCESS)
  } catch (error) {
    onError(apiMessages.DAY_REMOVE_FAIL)
    console.error('Error deleting day:', error)
  }
}

export const moveDay = async (
  { state, dispatch },
  { dayId, direction, onSuccess = () => {}, onError = () => {} },
) => {
  const itineraryId = state.itinerary.id
  try {
    await api.post(`/api/planner/day/${dayId}/move/${direction}/`)
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.MOVE_DAY_SUCCESS)
  } catch (error) {
    onError(apiMessages.MOVE_DAY_FAIL)
    console.error('Error moving day:', error)
  }
}
