
from threading import Timer

from model.bin import Bin
from model.belt import Belt
from enum import Enum

class Switch(Enum):
    """Swicth Enum"""
    ON = "ON"
    OFF = "OFF"
    PAUSE = "PAUSE"

class Factory:
    """Factory Class"""
    def __init__(self):
        self._belt = Belt()
        self._bin = Bin()
        self._switch = Switch.OFF
        self._timer = Timer(self._interval, self._time_interval)
        self._timer.start()


    def switch(self, state):
        self._switch = state







