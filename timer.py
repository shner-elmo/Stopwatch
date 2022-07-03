import time


class Timer:
    def __init__(self):
        self.timer_start = time.perf_counter()

    @property
    def time_elapsed(self):
        return time.perf_counter() - self.timer_start
