import unittest
import time

from src.stopwatch import Stopwatch

# finish testing
sw1 = Stopwatch()
sw1.start()
time.sleep(0.03)
sw2 = Stopwatch()
sw2.start()
time.sleep(0.11)
x = sw2.time_elapsed()
print(sw2 + sw1)
print(sw1 - sw2)
print(sw2 + 4.53)
print(sw2 - 4.342)
print(type(x))
print(type(sw2))
