import unittest
import task3


class TestCars(unittest.TestCase):
    def test_car_name_empty5(self):
        self.assertNotEqual(task3.sport.name == (""), 'Write something here')

    def test_car_not_equal_attributes6(self):
        self.assertIsNot(task3.sport.name, task3.sport.color)

    def test_raises7(self):
        with self.assertRaises(Exception):
            task3.WorkCar.speed > 300

    def test_raises8(self):
        self.assertNotIsInstance(task3.Car, task3.TownCar)



if __name__ == "__main__":
    unittest.main()
