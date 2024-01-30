// dayActions.js
import api from '@/api'

export const addDay = async ({ state, dispatch }, newDay) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(`/api/itinerary/${itineraryId}/day/`, newDay)
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error('Error adding day:', error)
  }
}

export const removeDay = async ({ state, dispatch }, dayId) => {
  const itineraryId = state.itinerary.id

  try {
    await api.delete(`/api/itinerary/${itineraryId}/day/${dayId}/`)
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
      `/api/itinerary/${itineraryId}/day/${dayId}/move/${moveDirection}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error('Error moving day:', error)
  }
}
