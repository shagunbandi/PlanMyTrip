from enum import Enum


class RESERVATION_STATUS(Enum):
    NO = "no"
    MAYBE = "maybe"
    YES = "yes"
    BOOKED = "booked"


class CHECKED_STATUS(Enum):
    SELECTED = "selected"
    CROSSED = "crossed"
    UNSELECTED = "unselected"
