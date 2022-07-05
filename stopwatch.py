import time
from typing import TypedDict, List, Dict
from exceptions import NotStartedYet, AlreadyStarted, AlreadyStopped


class StopwatchSplitDict(TypedDict):
    total: float
    time: float


class Stopwatch:
    """
    A class that behaves like a stopwatch

    To start and stop the counter call start() and stop() respectively,
    you can start and stop the same instance multiple times, and at any
    given moment you can check the total time elapsed by calling time_elapsed()
    which will return a float.

    You can also add splits by calling split() which will add a dictionary containing
    the total elapsed time, and the difference between the current and previous split
    to the attribute 'splits'.
    """
    def __init__(self):
        self.checkpoints: List[Dict] = []
        self.splits: List[Dict] = []

    def start(self) -> None:
        """
        Start the counter

        :return: None
        """
        if self.checkpoints:
            started = self.checkpoints[-1].get('start')
            stopped = self.checkpoints[-1].get('stop')
            if started and not stopped:
                raise AlreadyStarted('Stopwatch already started')

        self.checkpoints.append({'start': time.perf_counter()})

    def stop(self) -> None:
        """
        Stop the counter

        :return: None
        """
        if not self.checkpoints:
            raise NotStartedYet("Cannot stop a Stopwatch that hasn't been started")

        elif self.checkpoints[-1].get('stop'):
            raise AlreadyStopped('Stopwatch already stopped')

        self.checkpoints[-1]['stop'] = time.perf_counter()

    def time_elapsed(self) -> float:
        """
        Return the total elapsed time as a float number

        :return: float
        """
        if not self.checkpoints:
            return 0.0

        total_time_elapsed = 0
        for checkpoint in self.checkpoints:
            checkpoint_end = checkpoint.get('stop') or time.perf_counter()
            total_time_elapsed += checkpoint_end - checkpoint['start']

        return total_time_elapsed

    def split(self) -> None:
        """
        Add a split to self.splits containing the total elapsed time and the difference
        between current split and previous split.

        :return: None
        """
        total_time_elapsed = self.time_elapsed()

        last_time_elapsed = self.splits[-1]['total'] if self.splits else 0
        time_between_laps = total_time_elapsed - last_time_elapsed

        x: StopwatchSplitDict = {'total': total_time_elapsed, 'time': time_between_laps}
        self.splits.append(x)

    def reset(self) -> None:
        """
        Reset the elapsed time counter, and splits

        :return: None
        """
        self.__init__()

    def __add__(self, other) -> float:
        if isinstance(other, Stopwatch):
            return self.time_elapsed() + other.time_elapsed()

    def __sub__(self, other) -> float:
        if isinstance(other, Stopwatch):
            return self.time_elapsed() - other.time_elapsed()

    def __str__(self) -> str:
        return f"Time elapsed: {self.time_elapsed()}"

    def __repr__(self) -> str:
        return "Stopwatch()"

# finish testing
