
class Machine:
    """Machine interface"""
    def power(self, state):
        pass

class PulseMachine(Machine):
    """PulseMachine interface"""
    def power(self, state):
        pass

    def pulse(self):
        pass
 
