from model.cookie import Dollop, Cookie

class Stamper(PulseMachine):
    """ """
    def __init__(self):
        self._power = False

    def power(self, state = True):
        self._power = state
    
    def pulse(self):
        if self._power:
            self._stamp()

    def _stamp(self, obj):
        if isinstance(obj, Dollop):
            return Cookie()