from dataclasses import dataclass


class SnowType:
    pass


@dataclass
class Number(SnowType):
    value: any
    start: any
    end: any
    type = "Number"
    callable = False


@dataclass
class Bool(SnowType):
    value: bool
    start: any
    end: any
    type = "Bool"
    callable = False


@dataclass
class Void(SnowType):
    start: any
    end: any
    value: str = "Void"
    type = "Void"
    callable = False


@dataclass
class Function(SnowType):
    start: any
    end: any
    name: any
    args: any
    body: any
    type = "Function"
    callable = True

    @property
    def value(self):
        return self.__repr__()
