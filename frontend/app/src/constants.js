export const RESERVATION_KEYS = {
  CHECKED_STATUS: 'checked_status',
  NAME: 'name',
  NOTES: 'notes',
  ORDER: 'order',
  RESERVATION_PLACE_ID: 'reservation_place_id',
  RESERVATION_COST: 'reservation_cost',
  RESERVATION_LINK: 'reservation_link',
  RESERVATION_DATE: 'reservation_date',
  RESERVATION_TIME: 'reservation_time',
  RESERVATION_STATUS: 'reservation_status',
  RESERVATION_FILE: 'reservation_file',
}

export const ATTRACTION_KEYS = {
  ATTRACTION_TYPE: 'category',
  ...RESERVATION_KEYS,
}

export const CHECKED_STATUS = {
  UNSELECTED: 'UNSELECTED',
  SELECTED: 'SELECTED',
  CROSSED: 'CROSSED',
}

export const RESERVATION_STATUS = {
  NO: 'no',
  MAYBE: 'maybe',
  YES: 'yes',
  BOOKED: 'booked',
}

export const ATTRACTION_ENUM = {
  OTHER: 'other',
  HIKING: 'hiking',
  MONUMENT: 'monument',
  CLASSES: 'classes',
  LOCALITY: 'locality',
  EXPERIENCE: 'experience',
}
