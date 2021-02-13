from park.vehicle.vehicle import Vehicle
from park.constants import VehicleType


class Car(Vehicle):
    def __init__(self, registration_no):
        super().__init__(registration_no)

    def get_type(self):
        return VehicleType.CAR
