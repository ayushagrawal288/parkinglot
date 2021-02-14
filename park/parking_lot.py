import bisect
from park.parking_spot import ParkingSpot
from park.vehicle.vehicle import Vehicle
from park.ticket import Ticket
from collections import deque


class ParkingLot(object):
    '''
    Class is responsible for maintaining a complete parking lot
    containing n no of parking spots
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.next_spot_id = 0
        self.cur_occupied = 0
        self.spots = {}
        self.free_spot_ids = deque()

    def __get_next_spot_id(self):
        self.next_spot_id += 1
        return self.next_spot_id

    def _get_spot_id(self):
        if len(self.free_spot_ids) > 0:
            return self.free_spot_ids.popleft()
        return self.__get_next_spot_id()

    def _free_spot_id(self, spot_id):
        bisect.insort(self.free_spot_ids, spot_id)

    def occupy_spot(self, vehicle: Vehicle, driver_age: int):
        if self.cur_occupied == self.capacity:
            raise RuntimeError("Parking lot is full")
        ticket = Ticket(vehicle, driver_age)
        spot_id = self._get_spot_id()
        spot = ParkingSpot(spot_id)
        try:
            spot.park(ticket)
        except RuntimeError as e:
            return self.occupy_spot(vehicle, driver_age)
        self.spots[spot_id] = spot
        self.cur_occupied += 1
        return spot

    def empty_spot(self, spot_id):
        spot: ParkingSpot = self.spots.pop(spot_id, None)
        if spot is None:
            return None
        spot.leave()
        self._free_spot_id(spot.spot_id)
        self.cur_occupied -= 1
        return spot

    def get_all_occupied_spots(self):
        return list(self.spots.values())

