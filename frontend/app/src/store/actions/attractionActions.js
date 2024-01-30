// attractionActions.js
import api from '@/api'

export const addAttraction = async (
  { state, dispatch },
  { dayId, newAttraction },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/itinerary/${itineraryId}/day/${dayId}/attraction/`,
      newAttraction,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error('Error adding attraction:', error)
  }
}

export const removeAttraction = async (
  { state, dispatch },
  { dayId, attractionId },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.delete(
      `/api/itinerary/${itineraryId}/day/${dayId}/attraction/${attractionId}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error('Error removing attraction:', error)
  }
}

export const moveAttraction = async (
  { state, dispatch },
  { dayId, attractionId, moveDirection },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/itinerary/${itineraryId}/day/${dayId}/attraction/${attractionId}/move/${moveDirection}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error('Error moving attraction:', error)
  }
}
