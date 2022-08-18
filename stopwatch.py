from __future__ import annotations
import time

from enum import Enum
from typing import TypedDict, List, Dict, Callable

from exceptions import AlreadyStartedError, NotStartedYetError, AlreadyStoppedError, LapError


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
    given moment you can check the total elapsed time with the
    'time_elapsed' attribute which will return a float.

    You can also add laps by calling lap() which will add a dictionary containing
    the total elapsed time, and the difference between the current lap and previous lap
    to the attribute 'laps'.
    """

    def __init__(self) -> None:
        self.status: Status | None = None
        self._last_time_stamp: float = 0
        self._tot_time_elapsed: float = 0
        self.laps: List[Dict] = []

    def start(self) -> float:
        """
        Start the counter and return the current time-stamp (time.perf_counter())

        :return: float
        """
        if self.status == Status.active:
            raise AlreadyStartedError('Stopwatch already started')

        self.status = Status.active
        self._last_time_stamp = time.perf_counter()
        return time.perf_counter()

    def stop(self) -> float:
        """
        Stop the counter and return the current time-stamp (time.perf_counter())

        :return: float
        """
        if self.status is None:
            raise NotStartedYetError("Cannot stop a Stopwatch that hasn't been started")

        if self.status == Status.paused:
            raise AlreadyStoppedError('Stopwatch already stopped')

        self._tot_time_elapsed += time.perf_counter() - self._last_time_stamp
        self.status = Status.paused
        return time.perf_counter()

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

    def __enter__(self) -> Stopwatch:
        """

        :return:
        """
        self.start()
        return self

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


def time_it(stopwatch: Stopwatch = None):
    """
    A decorator for getting the time taken to execute a function/method

    If an instance of Stopwatch is passed it will add the time taken to run
    the code to the instance, and return: (time_elapsed, return_val)
    If no instance is passed, it will just return: (time_elapsed, return_val)

    :param stopwatch: instance of Stopwatch, optional
    :return:
    """
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):

            if stopwatch is not None:
                start = stopwatch.start()
                rv = func(*args, **kwargs)
                stop = stopwatch.stop()
                return stop - start, rv
            else:
                s = Stopwatch()
                s.start()
                rv = func(*args, **kwargs)
                return s.time_elapsed, rv

        return wrapper
    return decorator
