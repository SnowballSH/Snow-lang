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
        return str('"' + self.value + '"')


@dataclass
class BoolNode:
    def __init__(self, value):
        self.value = [True, False][value == "False"]

    def __repr__(self):
        return str(self.value)


@dataclass
class NullNode:
    def __init__(self):
        self.value = None

    def __repr__(self):
        return str(self.value)


@dataclass
class CompNode:
    left: any
    op: any
    right: any

    def __repr__(self):
        return f"({self.left}{self.op[1]}{self.right})"


@dataclass
class OpNode:
    left: any
    op: any
    right: any

    def __repr__(self):
        return f"({self.left}{self.op[1]}{self.right})"


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
class IfNode:
    cond: any
    then: any
    else_: any = None
    mode: any = None

    def __repr__(self):
        if self.mode == "KW":
            return f"if {self.cond}""{"f"{' '.join(repr(a) for a in self.then)}" + \
                   (f" else {' '.join(repr(a) for a in self.else_)}" if self.else_ else "") + "}"
        else:
            return f"?{self.cond}""{"f"{' '.join(repr(a) for a in self.then)} {' '.join(repr(a) for a in self.else_)}"\
                   "}"


@dataclass
class ForNode:
    var: any
    stop: any
    action: any
    body: any

    def __repr__(self):
        return f"for({self.var} {self.stop} {self.action})""{"f"{' '.join(repr(a) for a in self.body)}""}"


@dataclass
class BreakNode:
    def __repr__(self):
        return f"break"


@dataclass
class AccessMethodNode:
    parent: any
    child: any

    def __repr__(self):
        return f"{self.parent}.{self.child}"


@dataclass
class VarAssignNode:
    name: any
    value: any

    def __repr__(self):
        return f"{self.name[1]}={self.value}"


@dataclass
class VarAccessNode:
    name: any

    def __repr__(self):
        return f"{self.name[1]}"


@dataclass
class FuncAccessNode:
    name: any
    parameters: any

    def __repr__(self):
        return f"{self.name[1]}({' '.join(repr(a) for a in self.parameters)})"


@dataclass
class FuncAssignNode:
    name: any
    parameters: any
    call: any

    def __repr__(self):
        return f"def {self.name[1]}({' '.join(repr(a) for a in self.parameters)}) ""{"\
               f"{' '.join(repr(a) for a in self.call)}""}"


@dataclass
class AnonFuncAssignNode:
    name: any
    parameters: any
    call: any

    def __repr__(self):
        return f"def *({' '.join(repr(a) for a in self.parameters)}) ""{"f"{' '.join(repr(a) for a in self.call)}""}"


@dataclass
class GiveNode:
    expr: any

    def __repr__(self):
        return f"give {self.expr}"
