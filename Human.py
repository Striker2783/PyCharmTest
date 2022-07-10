from enum import Enum


class Human(object):
    def __init__(self, height, weight, hairColor):
        self.height = height
        self.weight = weight
        self.hairColor = hairColor


class HairColor(Enum):
    RED = 1
    BLUE = 2
    BROWN = 3
