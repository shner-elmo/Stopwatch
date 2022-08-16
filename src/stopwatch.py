from __future__ import annotations
import time

from enum import Enum
from typing import TypedDict, List, Dict

from .exceptions import AlreadyStartedError, NotStartedYetError, AlreadyStoppedError, LapError


class StopwatchLapDict(TypedDict):
    total: float
    time: float


class Status(Enum):
    active = 0
    paused = 1


class Stopwatch:
    """
    A class that behaves like a stopwatch

    To start and stop the counter call start() and stop() respectively,
    you can start and stop the same instance multiple times, and at any
    given moment you can check the total time elapsed the time_elapsed attribute
    which will return a float.

    You can also add laps by calling lap() which will add a dictionary containing
    the total elapsed time, and the difference between the current lap and previous lap
    to the attribute 'laps'.
    """

    def __init__(self) -> None:
        self.status: Status | None = None
        self._last_time_stamp: float = 0
        self._tot_time_elapsed: float = 0
        self.laps: List[Dict] = []

    def start(self) -> None:
        """
        Start the counter

        :return: None
        """
        if self.status == Status.active:
            raise AlreadyStartedError('Stopwatch already started')

        self.status = Status.active
        self._last_time_stamp = time.perf_counter()

    def stop(self) -> None:
        """
        Stop the counter

        :return: None
        """
        if self.status is None:
            raise NotStartedYetError("Cannot stop a Stopwatch that hasn't been started")

        if self.status == Status.paused:
            raise AlreadyStoppedError('Stopwatch already stopped')

        self._tot_time_elapsed += time.perf_counter() - self._last_time_stamp
        self.status = Status.paused

    @property
    def time_elapsed(self) -> float:
        """
        Return the total elapsed time as a float number

        :return: float
        """
        if self.status is None or self.status == Status.paused:
            return self._tot_time_elapsed

        elif self.status == Status.active:
            return self._tot_time_elapsed + (time.perf_counter() - self._last_time_stamp)

    def lap(self) -> None:
        """
        Add a lap to 'self.laps' containing the total elapsed time and the difference
        between current lap and previous lap.

        :return: None
        """
        if self.status is None or self.status == Status.paused:
            raise LapError('Cannot add a lap while Stopwatch is paused')

        total_time_elapsed = self.time_elapsed

        last_time_elapsed = self.laps[-1]['total'] if self.laps else 0
        time_between_laps = total_time_elapsed - last_time_elapsed

        x: StopwatchLapDict = {'total': total_time_elapsed, 'time': time_between_laps}
        self.laps.append(x)

    def reset(self) -> None:
        """
        Reset the elapsed time counter, and laps

        :return: None
        """
        self.__init__()

    def __enter__(self) -> None:
        """

        :return:
        """
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.stop()

    def __add__(self, other: Stopwatch | float) -> float:
        """
        Return the total time elapsed between the two instances, or time elapsed + float

        :param other: float or Stopwatch instance
        :return: float
        """
        if isinstance(other, Stopwatch):
            return self.time_elapsed + other.time_elapsed
        return self.time_elapsed + other

    def __sub__(self, other: Stopwatch | float) -> float:
        """
        Subtract the time elapsed of instance1 from instance2, or time elapsed - float

        :param other: float or Stopwatch instance
        :return: float
        """
        if isinstance(other, Stopwatch):
            return self.time_elapsed - other.time_elapsed
        return self.time_elapsed - other

    def __str__(self) -> str:
        """ Return a nicely formatted string with the total time elapsed """
        return f"Time elapsed: {self.time_elapsed:.3f}"

    def __repr__(self) -> str:
        """ Return a nicely formatted string with the total time elapsed """
        return f"Time elapsed: {self.time_elapsed:.3f}"


if __name__ == '__main__':
    def func(n=10_000_000):
        return [x for x in range(n)]

    sw = Stopwatch()

    with sw:
        func(1_000_000)

    print(sw.time_elapsed)

    with sw:
        func(5_000_000)

    print(sw.time_elapsed)

