"""
Public and Private
By default, all properties and methods in a class are public. That means that you can access them with the . operator:
"""

wall.height = 10
print(wall.height)
# 10
"""
Private data members are a way to encapsulate logic and data within a class definition. To make a property or method private just prefix it with two underscores:
"""
class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance

front_wall = Wall(10, 20)

# This results in an error
print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30

## ASSIGNMENT ##
class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = 100 * stamina
        self.mana = 10 * intelligence
        pass
