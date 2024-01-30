// dayActions.js
import api from '@/api'

export const addDay = async ({ commit, state }, newDay) => {
  const itineraryId = state.itinerary.id

  try {
    const response = await api.post(
      `/api/itinerary/${itineraryId}/day/`,
      newDay,
    )
    const updatedItinerary = { ...state.itinerary }
    updatedItinerary.days.push(response.data)

    commit('SET_ITINERARY', updatedItinerary)
  } catch (error) {
    console.error('Error adding day:', error)
  }
}

export const removeDay = async ({ commit, state }, dayId) => {
  const itineraryId = state.itinerary.id

  try {
    await api.delete(`/api/itinerary/${itineraryId}/day/${dayId}/`)
    const updatedItinerary = { ...state.itinerary }
    updatedItinerary.days = updatedItinerary.days.filter(
      (day) => day.id !== dayId,
    )

    commit('SET_ITINERARY', updatedItinerary)
  } catch (error) {
    console.error('Error removing day:', error)
  }
}

export const moveDay = async (
  { commit, state, dispatch },
  { dayId, moveDirection },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/itinerary/${itineraryId}/day/${dayId}/move/${moveDirection}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error('Error moving day:', error)
    commit('SET_ERROR', error.message || 'Error moving day')
  }
}
