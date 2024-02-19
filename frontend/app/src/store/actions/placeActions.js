// commonPlaceActions.js
import api from '@/api'
import apiMessages from '@/constants/apiMessages'

export const addPlace = async (
  { state, dispatch },
  {
    title = 'Title',
    contentType,
    parentId,
    onSuccess = () => {},
    onError = () => {},
  },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(`/api/planner/place/`, {
      title: title,
      content_type: contentType,
      object_id: parentId,
    })
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.PLACE_ADD_SUCCESS)
  } catch (error) {
    console.error(`Error adding ${title}:`, error)
    onError(apiMessages.PLACE_ADD_FAIL)
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
