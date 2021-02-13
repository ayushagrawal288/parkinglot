from park.vehicle.vehicle import Vehicle
from park.constants import TicketStatus


class Ticket(object):
    def __init__(self, vehicle: Vehicle, driver_age: int):
        self.vehicle = vehicle
        self.driver_age = driver_age
        self.status = TicketStatus.ACTIVE

    def return_ticket(self):
        self.status = TicketStatus.COMPLETE
