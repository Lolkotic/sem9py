import unittest
import task2


class TestWorker(unittest.TestCase):
    def test_worker2(self):
        self.assertNotEqual(task2.p.get_total_income(), 10000)

    def test_worker3(self):
        self.assertIsNotNone(task2.p.get_total_income(), "You forgot to write your numbers!")

    def test_worker4(self):
        self.assertIsInstance(task2.p.get_full_name(), str)


if __name__ == "__main__":
    unittest.main()

