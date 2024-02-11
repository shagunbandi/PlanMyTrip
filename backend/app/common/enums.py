from enum import Enum


class RESERVATION_STATUS(Enum):
    NO = "no"
    MAYBE = "maybe"
    BOOKED = "booked"
    UNSET = None
