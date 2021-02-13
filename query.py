from park.parking_lot import ParkingLot
from utils import age_filter_parking_lot, reg_no_parking_lot


class Query(object):
    def __init__(self, lot: ParkingLot):
        self.lot = lot

    def get_reg_no_for_cars(self, driver_age: int):
        '''
        Fetches all vehicles for whom driver age is equal to passed age
        :param driver_age:
        :return: list of registration nos
        '''
        spots = self.lot.get_all_occupied_spots()
        cust_filter = age_filter_parking_lot(driver_age)
        filtered_spots = list(filter(cust_filter, spots))
        return [x.get_vehicle_reg_no() for x in filtered_spots]

    def get_slot_for_reg_no(self, reg_no: str):
        '''
        Fetches parking slot no for a given registration number
        :param reg_no:
        :return: parking spot no
        '''
        spots = self.lot.get_all_occupied_spots()
        cust_filter = reg_no_parking_lot(reg_no)
        filtered_spots = list(filter(cust_filter, spots))
        if len(filtered_spots) == 0:
            return None
        return filtered_spots[0].spot_id

    def get_slot_for_drivers(self, driver_age: int):
        '''
        Fetches all vehicles for whom driver age is equal to passed age
        :param driver_age:
        :return: list of spot nos
        '''
        spots = self.lot.get_all_occupied_spots()
        cust_filter = age_filter_parking_lot(driver_age)
        filtered_spots = list(filter(cust_filter, spots))
        return [x.spot_id for x in filtered_spots]
