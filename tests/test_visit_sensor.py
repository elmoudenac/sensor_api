from fake_data_app.sensor import VisitSensor
import unittest
from datetime import date


class TestVisitSensor(unittest.TestCase):
    def test_monday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2025,4,21))

        self.assertFalse(visit_count == -1)

    def test_tuesday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2025,4,22))

        self.assertFalse(visit_count == -1)

    def test_wednesday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2025, 4, 23))

        self.assertFalse(visit_count == -1)

    def test_thursday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2025, 4, 24))

        self.assertFalse(visit_count == -1)

    def test_friday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2025, 4, 25))

        self.assertFalse(visit_count == -1)

    def test_saturday_open(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2025, 4, 26))

        self.assertFalse(visit_count == -1)

    def test_sunday_closed(self):
        visit_sensor = VisitSensor(1200, 300)
        visit_count = visit_sensor.simulate_visit_count(date(2025, 4, 27))

        self.assertEqual(visit_count, -1)

    def test_with_break(self):
        visit_sensor = VisitSensor(1200,300,perc_break=10)
        visit_count = visit_sensor.get_visit_count(date(2023,10,22))
        self.assertEqual(visit_count,0)

    def test_with_malfunction(self):
        visit_sensor = VisitSensor(1200,300,perc_malfunction=10)
        visit_count = visit_sensor.get_visit_count(date(2023,11,28))
        self.assertEqual(visit_count,238)


if __name__ == '__main__':
    unittest.main()