from typing import Dict, List
from model.cookie import Cookie


class Oven:
    """Oven class"""
    
    DEG_PER_INTERVAL_HEATING = 50
    DEG_PER_INTERVAL_COOLING = -20
    DEG_AMBIENT_TEMPERATURE = 20

    COOKIE_BAKE_RANGE = [220, 240]

    def __init__(self):
        self._power = False
        self._temp = DEG_AMBIENT_TEMPERATURE
        self._interval = 1

    def action(self, obj):
        if isinstance(obj, Cookie):
            if self._temp < COOKIE_BAKE_RANGE[0]:
                pass
            elif self._temp >= COOKIE_BAKE_RANGE[1]:
                obj.percentage_baked += 0.8
            else:
                obj.percentage_baked += 0.3
        
        return obj
        
    def power(self, state):
        state._power_on = state

    def time_interval(self):
        if self._power:
            if self._temp < COOKIE_BAKE_RANGE[1]:
                self._temp = self._temp + DEG_PER_INTERVAL_HEATING
        else:
            self._temp = self._temp + DEG_PER_INTERVAL_HEATING



