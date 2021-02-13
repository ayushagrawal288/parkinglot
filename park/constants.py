import enum


class TicketStatus(enum.Enum):
    ACTIVE = 1
    COMPLETE = 2


class VehicleType(enum.Enum):
    CAR = 1


class SpotType(enum.Enum):
    FREE = 1
    OCCUPIED = 2
