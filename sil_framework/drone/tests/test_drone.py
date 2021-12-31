
from sil_framework.drone.drone import Drone


class TestDrone:

    @staticmethod
    def create_unit_under_test():
        return Drone()

    def test_interface(self):
        assert self.create_unit_under_test() is not None

    def test_example_public_method_1(self):
        unit_under_test = self.create_unit_under_test()
        assert unit_under_test.example_public_method_1() == 1

    def test_example_public_method_2(self):
        unit_under_test = self.create_unit_under_test()
        assert unit_under_test.example_public_method_2() == 2
