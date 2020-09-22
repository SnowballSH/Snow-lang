from dataclasses import dataclass


@dataclass
class Number:
    value: any
    start: any
    end: any
    type = "Number"


@dataclass
class Void:
    start: any
    end: any
    value: str = "Void"
    type = "Void"
