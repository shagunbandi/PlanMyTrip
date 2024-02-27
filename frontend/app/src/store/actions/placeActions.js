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

export const editPlaceField = async (
  { state, dispatch },
  {
    contentType,
    objectId,
    placeId,
    fieldName,
    fieldValue,
    onSuccess = () => {},
    onError = () => {},
  },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.patch(`/api/planner/place/${placeId}/`, {
      [fieldName]: fieldValue,
      content_type: contentType,
      object_id: objectId,
    })
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.PLACE_UPDATE_SUCCESS)
  } catch (error) {
    console.error(`Error updating ${fieldName}:`, error)
    onError(apiMessages.PLACE_UPDATE_FAILED)
  }
}

export const removePlace = async (
  { state, dispatch },
  { placeId, placeName, onSuccess = () => {}, onError = () => {} },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.delete(`/api/planner/place/${placeId}/`)
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.PLACE_REMOVE_SUCCESS)
  } catch (error) {
    onError(apiMessages.PLACE_REMOVE_FAILED)
    console.error(`Error removing ${placeName}:`, error)
  }
}

export const movePlace = async (
  { state, dispatch },
  {
    contentType,
    objectId,
    placeId,
    moveDirection,
    onSuccess = () => {},
    onError = () => {},
  },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/planner/place/${placeId}/move/${moveDirection}/?${contentType}=${objectId}`,
    )
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.PLACE_MOVE_SUCCESS)
  } catch (error) {
    onError(apiMessages.PLACE_MOVE_FAILED)
    console.error(`Error moving ${placeId}:`, error)
  }
}
