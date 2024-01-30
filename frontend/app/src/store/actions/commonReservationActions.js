// commonReservationActions.js
import api from '@/api'

export const addReservation = async (
  { state, dispatch },
  { dayId, newReservation, reservationName },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/itinerary/${itineraryId}/day/${dayId}/${reservationName}/`,
      newReservation,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error(`Error adding ${reservationName}:`, error)
  }
}

export const removeReservation = async (
  { state, dispatch },
  { dayId, reservationId, reservationName },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.delete(
      `/api/itinerary/${itineraryId}/day/${dayId}/${reservationName}/${reservationId}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error(`Error removing ${reservationName}:`, error)
  }
}

export const moveReservation = async (
  { state, dispatch },
  { dayId, reservationId, reservationName, moveDirection },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/itinerary/${itineraryId}/day/${dayId}/${reservationName}/${reservationId}/move/${moveDirection}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error(`Error moving ${reservationName}:`, error)
  }
}
