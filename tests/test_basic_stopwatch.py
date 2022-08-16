from src.basic_stopwatch import Stopwatch as Sw
import unittest
import time


class TestBasicStopwatch(unittest.TestCase):
    """ Class for testing the basic Stopwatch """

    def test_init(self):
        self.assertNotEqual(Sw().timer_start, 0)

    def test_time_elapsed(self):
        self.assertGreater(Sw().time_elapsed, 0.0)
        x = Sw()
        self.assertAlmostEqual(x.time_elapsed, time.perf_counter() - x.timer_start, delta=0.05)
        self.assertAlmostEqual(Sw().time_elapsed, 0, delta=0.05)  # delta ?


if __name__ == '__main__':
    unittest.main()
