
class StopwatchException(Exception):
    """ Base Stopwatch exception """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class AlreadyStarted(StopwatchException):
    """ Thrown when Stopwatch.start() is called more than once in a row """
    pass


class NotStartedYet(StopwatchException):
    """ Thrown when the Stopwatch is not started yet and the user tries to stop it """
    pass


class AlreadyStopped(StopwatchException):
    """ Thrown when Stopwatch.stop() is called more than once in a row """
    pass
