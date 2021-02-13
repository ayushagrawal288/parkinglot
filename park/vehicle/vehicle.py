import abc


class Vehicle(object, metaclass=abc.ABCMeta):
    def __init__(self, registration_no):
        self.registration_no = registration_no

    @abc.abstractmethod
    def get_type(self):
        raise NotImplementedError("Need to implement this method")
