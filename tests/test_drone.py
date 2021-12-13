
from source.drone import Drone


class TestDrone:

    @staticmethod
    def create_unit_under_test():
        return Drone()

    def test_interface(self):
        assert self.create_unit_under_test() is not None
