from enum import Flag, auto

class PAN(Flag):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


def Pan(direction: PAN):
    if direction == PAN.DOWN:
        pass
    elif direction == PAN.UP:
        pass
    elif direction == PAN.LEFT:
        pass
    elif direction == PAN.RIGHT:
        pass
    else:
        pass
