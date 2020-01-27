# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # base class
    pass

class FlightVehicle(Vehicle):
    # base class
    pass

class Starship(FlightVehicle):
    # subclass
    pass

class Airplane(FlightVehicle):
    # subclass
    pass
class GroundVehicle(Vehicle):
    # base class
    pass

class Car(GroundVehicle):
    # subclass
    pass

class Motorcycle(GroundVehicle):
    # subclass
    pass

