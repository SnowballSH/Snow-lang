from dataclasses import dataclass


class SnowType:
    pass


@dataclass
class Number(SnowType):
    value: any
    start: any
    end: any
    type = "Number"


@dataclass
class Void(SnowType):
    start: any
    end: any
    value: str = "Void"
    type = "Void"
