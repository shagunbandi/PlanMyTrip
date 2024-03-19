// commonPlaceActions.js
import api from '@/api'
import apiMessages from '@/constants/apiMessages'

export const addPlace = async (
  { state, dispatch },
  { agendaId, title = '', onSuccess = () => {}, onError = () => {} },
) => {
  const planId = state.plan.id

  try {
    await api.post(`/api/planner/plan/${planId}/agenda/${agendaId}/place/`, {
      title: title,
    })
    dispatch('fetchPlan', { planId })
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
  const planId = state.plan.id
  const postData = Array.isArray(fieldName)
    ? fieldName.reduce((acc, key, index) => {
        acc[key] = fieldValue[index]
        return acc
      }, {})
    : { [fieldName]: fieldValue }

  try {
    await api.patch(
      `/api/planner/plan/${planId}/agenda/${agendaId}/place/${placeId}/`,
      postData,
    )
    dispatch('fetchPlan', { planId })
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
  const planId = state.plan.id
  try {
    await api.delete(
      `/api/planner/plan/${planId}/agenda/${agendaId}/place/${placeId}/`,
    )
    dispatch('fetchPlan', { planId })
    onSuccess(apiMessages.PLACE_REMOVE_SUCCESS)
  } catch (error) {
    onError(apiMessages.PLACE_REMOVE_FAILED)
    console.error(`Error deleting ${placeId}`, error)
  }
}

export const movePlace = async (
  { state, dispatch },
  { placeId, agendaId, method, onSuccess = () => {}, onError = () => {} },
) => {
  const planId = state.plan.id

  try {
    const postData = {
      method: method,
    }
    await api.post(
      `/api/planner/plan/${planId}/agenda/${agendaId}/place/${placeId}/move/`,
      postData,
    )
    dispatch('fetchPlan', { planId })
    onSuccess(apiMessages.PLACE_MOVE_SUCCESS)
  } catch (error) {
    onError(apiMessages.PLACE_MOVE_FAILED)
    console.error(`Error moving ${placeId}:`, error)
  }
}
