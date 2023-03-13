import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date(2023,3,10)
        last_service_date = date(2017,9,13)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date(2023,3,10)
        last_service_date = date(2021,9-13)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())