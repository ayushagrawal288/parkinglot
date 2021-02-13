from park.parking_spot import ParkingSpot


def age_filter_parking_lot(required_age: int):
    age = required_age

    def filter_custom(x: ParkingSpot):
        return x.get_driver_age() == age

    return filter_custom


def reg_no_parking_lot(reg_no: str):
    reg = reg_no

    def filter_custom(x: ParkingSpot):
        return x.get_vehicle_reg_no() == reg

    return filter_custom

