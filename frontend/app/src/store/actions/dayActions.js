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
    commit('SET_ERROR', error.message || 'Error adding day')
  }
}
