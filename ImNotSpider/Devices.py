from enum import Enum


class PlateForm(Enum):
    PC = 0
    WAP = 1


class PC(Enum):
    Linux = 0
    Mac = 1
    Windows = 2


class WAP(Enum):
    Android = 0
    Iphone = 1
    WindowsPhone = 2
