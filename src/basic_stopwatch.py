import time


class Stopwatch:
    """
    A class that behaves like a stopwatch, when initialized the counter starts,
    and at any given moment you can check the total time elapsed
    with the time_elapsed property
    """

    def __init__(self) -> None:
        self.timer_start = time.perf_counter()

    @property
    def time_elapsed(self) -> float:
        """ Return total time elapsed in seconds as a float """
        return time.perf_counter() - self.timer_start

    def __enter__(self) -> None:
        """ Starts the timer """
        self.__init__()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """ Prints the time elapsed """
        print(self)

    def __str__(self) -> str:
        """ Return time elapsed as a string """
        return f"Time elapsed: {self.time_elapsed:.3f}"

    def __repr__(self) -> str:
        """ Return time elapsed as a string """
        return f"Time elapsed: {self.time_elapsed:.3f}"


if __name__ == '__main__':
    stopwatch = Stopwatch()
    lst = []
    for x in range(10_000_000):
        lst.append(x)
    print(stopwatch)

    # or:
    with Stopwatch():
        print('executing code...')
        lst = []
        for x in range(10_000_000):
            lst.append(x)
