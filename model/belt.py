from model.extruder import Extruder
from model.stamper import Stamper
from model.oven import Oven
from model.bin import Bin
from model.interfaces import Machine, PulseMachine

class Belt(Machine):
    """Belt class"""
    def __init__(self):
        self._power = False
        self._slots = [None] * 9

        extruder = Extruder()
        stamper = Stamper()
        oven = Oven()
        bin = Bin()

        self.machines = {
            "1": extruder.action,
            "3": stamper.action,
            "5": oven.action,
            "6": oven.action,
            "7": oven.action,
            "9": bin.action,
        }

    def power(self, state = True):
        self._power = state

    def _move(self):
        new_slots = []
        for slot, i in enumerate(self._slots):
            if machines.get(i):
                func = machines.get(i)
                new_slots.append(func(slot))
            else:
                new_slots.append(None)
        self._slots = new_slots

    def action(self):
        if self._power or self._slots != [None] * 9:
            _move()
            
