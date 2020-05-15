Design

Machine (Interface)
 power_on: bool

Oven (Machine)
 power_on: bool
 temp: int
 COOLING_RATE: 
 HEATING_RATE:
 action()

PulseMachine (Interface)
 pulse()

Extruder (PulseMachine)
 pulse() => make_dollop()

Stamper (PulseMachine)
 pulse() => stamp()

Belt (Machine)
 power_on: bool
 slots: list
 machines: dict
 action() => move()

Bin
 cookies: int
 action()

None
Dollop
Cookie
 pecentage_baked: float

Factory
 Belt
  Extruder
  Stamper
  Oven
  Oven
  Oven
 Bin
 Switch: On/Off/Pause: Enom
