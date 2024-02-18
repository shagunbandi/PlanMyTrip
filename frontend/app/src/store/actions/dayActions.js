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

export const removeDay = async ({ state, dispatch }, dayId) => {
  const itineraryId = state.itinerary.id
  try {
    await api.delete(`/api/planner/itinerary/${itineraryId}/day/${dayId}/`)
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error('Error removing day:', error)
  }
}

export const moveDay = async (
  { state, dispatch },
  { dayId, moveDirection },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/planner/itinerary/${itineraryId}/day/${dayId}/move/${moveDirection}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error('Error moving day:', error)
  }
}
