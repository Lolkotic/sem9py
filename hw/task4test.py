import unittest
import task4


class TestNumbers(unittest.TestCase):
    def test_num_exceptions9(self):
        with self.assertRaises(Exception):
            ValueError

    def test_num_not_none10(self):
        self.assertIsNotNone(task4.my_func)


if __name__ == "__main__":
    unittest.main()
