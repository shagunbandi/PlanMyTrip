// commonPlaceActions.js
import api from '@/api'
import apiMessages from '@/constants/apiMessages'

export const addPlace = async (
  { state, dispatch },
  { agendaId, title = '', onSuccess = () => {}, onError = () => {} },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.post(
      `/api/planner/itinerary/${itineraryId}/agenda/${agendaId}/place/`,
      {
        title: title,
      },
    )
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
    placeId,
    agendaId,
    fieldName,
    fieldValue,
    onSuccess = () => {},
    onError = () => {},
  },
) => {
  const itineraryId = state.itinerary.id

  try {
    await api.patch(
      `/api/planner/itinerary/${itineraryId}/agenda/${agendaId}/place/${placeId}/`,
      {
        [fieldName]: fieldValue,
      },
    )
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.PLACE_UPDATE_SUCCESS)
  } catch (error) {
    console.error(`Error updating ${fieldName} for ${placeId}:`, error)
    onError(apiMessages.PLACE_UPDATE_FAILED)
  }
}

export const removePlace = async (
  { state, dispatch },
  { placeId, agendaId, onSuccess = () => {}, onError = () => {} },
) => {
  const itineraryId = state.itinerary.id
  try {
    await api.delete(
      `/api/planner/itinerary/${itineraryId}/agenda/${agendaId}/place/${placeId}/`,
    )
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.PLACE_REMOVE_SUCCESS)
  } catch (error) {
    onError(apiMessages.PLACE_REMOVE_FAILED)
    console.error(`Error deleting ${placeId}`, error)
  }
}

export const movePlace = async (
  { state, dispatch },
  {
    placeId,
    method,
    parentId,
    parentContentType,
    onSuccess = () => {},
    onError = () => {},
  },
) => {
  const itineraryId = state.itinerary.id

  try {
    const postData = {
      content_type: 'place',
      method: method,
      parent_id: parentId,
      parent_content_type: parentContentType,
    }
    await api.post(`/api/planner/move/${placeId}/`, postData)
    dispatch('fetchItinerary', { itineraryId })
    onSuccess(apiMessages.PLACE_MOVE_SUCCESS)
  } catch (error) {
    onError(apiMessages.PLACE_MOVE_FAILED)
    console.error(`Error moving ${placeId}:`, error)
  }
}
