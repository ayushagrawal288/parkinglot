from park.constants import SpotType
from park.ticket import Ticket


class ParkingSpot(object):
    '''
    Class is responsible for maintaining a parking spot
    '''

    def __init__(self, spot_id):
        self.status = SpotType.FREE
        self.spot_id = spot_id
        self.ticket = None

    def park(self, ticket: Ticket):
        if self.status == SpotType.OCCUPIED:
            raise RuntimeError("Parking spot already taken")
        self.status = SpotType.OCCUPIED
        self.ticket = ticket

    def leave(self):
        self.status = SpotType.FREE
        self.ticket.return_ticket()

    def get_driver_age(self):
        return self.ticket.driver_age

    def get_vehicle_reg_no(self) -> str:
        return self.ticket.vehicle.registration_no
