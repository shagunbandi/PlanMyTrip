// commonPlaceActions.js
import api from '@/api'

export const addPlace = async (
  { state, dispatch },
  { dayId, newPlace, placeName },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/planner/itinerary/${itineraryId}/day/${dayId}/${placeName}/`,
      newPlace,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error(`Error adding ${placeName}:`, error)
  }
}

export const removePlace = async (
  { state, dispatch },
  { dayId, placeId, placeName },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.delete(
      `/api/planner/itinerary/${itineraryId}/day/${dayId}/${placeName}/${placeId}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error(`Error removing ${placeName}:`, error)
  }
}

export const movePlace = async (
  { state, dispatch },
  { dayId, placeId, placeName, moveDirection },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/planner/itinerary/${itineraryId}/day/${dayId}/${placeName}/${placeId}/move/${moveDirection}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error(`Error moving ${placeName}:`, error)
  }
}
