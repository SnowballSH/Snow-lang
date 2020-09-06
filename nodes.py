from dataclasses import dataclass


@dataclass
class ImportNode:
    package: any

    def __repr__(self):
        return f"import {self.package}"


@dataclass
class NumberNode:
    value: any

    def __repr__(self):
        return str(self.value)


@dataclass
class StringNode:
    value: str

    def __repr__(self):
        return str(self.value)


@dataclass
class CompNode:
    left: any
    op: any
    right: any

    def __repr__(self):
        return f"({self.left} {self.op[1]} {self.right})"


@dataclass
class OpNode:
    left: any
    op: any
    right: any

    def __repr__(self):
        return f"({self.left} {self.op[1]} {self.right})"


@dataclass
class UnaryOpNode:
    op: any
    right: any

    def __repr__(self):
        return f"{self.op[1]}{self.right}"


@dataclass
class PutNode:
    expr: any

    def __repr__(self):
        return f"put {self.expr}"


@dataclass
class GetNode:
    expr: any

    def __repr__(self):
        return f"get {self.expr}"


@dataclass
class VarAssignNode:
    name: any
    value: any

    def __repr__(self):
        return f"assign {self.name[1]} = {self.value}"


@dataclass
class VarAccessNode:
    name: any

    def __repr__(self):
        return f"access {self.name[1]}"


@dataclass
class FuncAccessNode:
    name: any
    parameters: any

    def __repr__(self):
        return f"access {self.name[1]} ({self.parameters})"


@dataclass
class FuncAssignNode:
    name: any
    parameters: any
    call: any

    def __repr__(self):
        return f"assign {self.name[1]} ({self.parameters}) => {self.call}"
