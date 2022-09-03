
class StopwatchException(Exception):
    """ Base Stopwatch exception """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class AlreadyStartedError(StopwatchException):
    """ Thrown when Stopwatch.start() is called more than once in a row """
    pass


class NotStartedYetError(StopwatchException):
    """ Thrown when the Stopwatch is not started yet and the user tries to stop it """
    pass


class AlreadyStoppedError(StopwatchException):
    """ Thrown when Stopwatch.stop() is called more than once in a row """
    pass


class LapError(StopwatchException):
    """ Thrown when Stopwatch.lap() is called while the stopwatch is paused """
    pass
