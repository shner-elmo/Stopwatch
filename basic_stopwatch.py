import time


class Stopwatch:
    """
    A class that behaves like a stopwatch, when initialized the counter starts,
    and at any given moment you can check the total time elapsed
    with the time_elapsed property
    """

    def __init__(self):
        self.timer_start = time.perf_counter()

    @property
    def time_elapsed(self) -> float:
        """ return total time elapsed in seconds as a float """
        return time.perf_counter() - self.timer_start
