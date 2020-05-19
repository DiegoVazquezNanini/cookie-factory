
from model.cookie import Dollop
from model.interfaces import PulseMachine

class Extruder(PulseMachine):
    """Extruder class"""
    def __init__(self):
         self._power = False

    def power(self, state = True):
        self._power = state

    def pulse(self):
        if self._power:
            self.make_dollop()

    def _make_dollop(self):
        return Dollop()
