from constants import *
from park.parking_lot import ParkingLot
from park.vehicle.car import Car
from query import Query


class ReadInput(object):
    parking_lot: ParkingLot

    def __init__(self, filepath):
        self.filename = filepath

    def process(self):
        with open(self.filename) as file_in:
            for line in file_in:
                self.command(line.rstrip())

    def command(self, cmd: str):
        command = cmd.lower().split(" ")
        if command[0] == CREATE_PARKING_LOT:
            self.create_lot(command[1:])
        elif command[0] == PARK_CAR:
            self.park(command[1:])
        elif command[0] == CAR_DEPARTURE:
            self.leave(command[1:])
        elif command[0] == SEARCH_SPOT_BY_CAR_NUMBER:
            self.get_slot_for_car_no(command[1:])
        elif command[0] == SEARCH_CAR_BY_AGE:
            self.search_car_by_age(command[1:])
        elif command[0] == SEARCH_SPOT_BY_AGE:
            self.search_spot_by_age(command[1:])
        else:
            print('Invalid command: ' + cmd)

    def check_parking_lot(self):
        if self.parking_lot is None:
            raise RuntimeError("Parking lot needs to be created before running other commands")

    def create_lot(self, args):
        if len(args) != 1:
            print(CREATE_PARKING_LOT + "command only accepts 1 argument: capacity")
            return
        size = int(args[0])
        self.parking_lot = ParkingLot(size)
        print("Created parking of " + str(size) + " slots")

    def park(self, args):
        self.check_parking_lot()
        if len(args) != 3:
            print(PARK_CAR + "command only accepts 3 argument: reg_no driver_age age")
            return
        if args[1] != DRIVER_AGE:
            print(PARK_CAR + "command's 2 argument should be: " + DRIVER_AGE)
            return
        reg_no = args[0]
        age = int(args[2])
        vehicle = Car(reg_no)
        try:
            spot = self.parking_lot.occupy_spot(vehicle, age)
            print(
                'Car with vehicle registration number "' + reg_no.upper() + '" has been parked at slot number ' + str(
                    spot.spot_id))
        except RuntimeError as e:
            print(e.__str__())

    def leave(self, args):
        self.check_parking_lot()
        if len(args) != 1:
            print(CAR_DEPARTURE + "command only accepts 1 argument: spot_id")
            return
        spot_id = int(args[0])
        spot = self.parking_lot.empty_spot(spot_id)
        if spot is None:
            print("Slot already vacant")
        else:
            print('Slot number ' + str(
                spot.spot_id) + ' vacated, the car with vehicle registration number "' + spot.get_vehicle_reg_no().upper() +
                  '" left the space, the driver of the car was of age ' + str(spot.get_driver_age()))

    def get_slot_for_car_no(self, args):
        self.check_parking_lot()
        if len(args) != 1:
            print(SEARCH_SPOT_BY_CAR_NUMBER + "command only accepts 1 argument: reg no")
            return
        reg_no = args[0]
        q = Query(self.parking_lot)
        res = q.get_slot_for_reg_no(reg_no)
        if res is None:
            print("null")
        else:
            print(res)

    def search_car_by_age(self, args):
        self.check_parking_lot()
        if len(args) != 1:
            print(SEARCH_CAR_BY_AGE + "command only accepts 1 argument: age")
            return
        age = int(args[0])
        q = Query(self.parking_lot)
        res = q.get_reg_no_for_cars(age)
        if len(res) == 0:
            print("null")
        else:
            print(','.join(x.upper() for x in res))

    def search_spot_by_age(self, args):
        self.check_parking_lot()
        if len(args) != 1:
            print(SEARCH_SPOT_BY_AGE + "command only accepts 1 argument: age")
            return
        age = int(args[0])
        q = Query(self.parking_lot)
        res = q.get_slot_for_drivers(age)
        if len(res) == 0:
            print("null")
        else:
            print(','.join(str(x) for x in res))
