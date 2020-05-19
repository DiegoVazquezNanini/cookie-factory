from model.cookie import Dollop, Cookie
from model.interfaces import PulseMachine

class Stamper(PulseMachine):
    """ """
    def __init__(self):
        self._power = False

    def power(self, state = True):
        self._power = state
    
    def pulse(self, obj):
        if self._power:
            self._stamp(obj)

    def _stamp(self, obj):
        if isinstance(obj, Dollop):
            return Cookie()