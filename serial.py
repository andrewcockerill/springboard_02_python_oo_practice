"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    Parameters
    ----------

    start : int, default=100
        The starting value to begin generating from

    Attributes
    ----------

    next : int
        The next integer that will be generated

    Methods
    -------
    generate():
        Returns the next number to be generated

    reset():
        Resets the next number to be generated to `start` value


    Examples
    --------

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        try:
            self._start = int(start)
            self._next = self._start
        except:
            raise ValueError("'start' must be an integer")

    @property
    def start(self):
        return self._start

    @property
    def next(self):
        return self._next

    def generate(self):
        out_value = self._next
        self._next += 1
        return out_value

    def reset(self):
        self._next = self._start

    def __repr__(self):
        return f"<SerialGenerator start={str(self._start)} next={str(self._next)}>"
