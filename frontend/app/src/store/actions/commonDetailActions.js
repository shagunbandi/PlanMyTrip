// commonDetailActions.js
import api from '@/api'

export const addDetail = async (
  { state, dispatch },
  { dayId, newDetail, detailName },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/itinerary/${itineraryId}/day/${dayId}/${detailName}/`,
      newDetail,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error(`Error adding ${detailName}:`, error)
  }
}

export const removeDetail = async (
  { state, dispatch },
  { dayId, detailId, detailName },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.delete(
      `/api/itinerary/${itineraryId}/day/${dayId}/${detailName}/${detailId}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error(`Error removing ${detailName}:`, error)
  }
}

export const moveDetail = async (
  { state, dispatch },
  { dayId, detailId, detailName, moveDirection },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/itinerary/${itineraryId}/day/${dayId}/${detailName}/${detailId}/move/${moveDirection}/`,
    )
    dispatch('fetchItinerary', itineraryId)
  } catch (error) {
    console.error(`Error moving ${detailName}:`, error)
  }
}
