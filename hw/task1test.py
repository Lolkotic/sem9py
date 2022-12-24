import unittest
import task1


class TestRoad(unittest.TestCase):
    def test_Road1(self):
        self.assertIsNone(task1.r.asphalt_mass())


if __name__ == "__main__":
    unittest.main()
