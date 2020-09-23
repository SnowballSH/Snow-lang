class Node:
    pass


class NumberNode(Node):
    def __init__(self, value, start, end):
        self.value = value
        self.start = start
        self.end = end
        self.type = "Number"

    def __repr__(self):
        return f"{self.value}"


class VarAccessNode(Node):
    def __init__(self, value, start, end):
        self.value = value
        self.start = start
        self.end = end
        self.type = "VarAccess"

    def __repr__(self):
        return f"{self.value}"


class VarAssignNode(Node):
    def __init__(self, name, value, start, end):
        self.name = name
        self.value = value
        self.start = start
        self.end = end
        self.type = "VarAssign"

    def __repr__(self):
        return f"{self.name} = {self.value}"


class WalrusVarAssignNode(Node):
    def __init__(self, name, value, start, end):
        self.name = name
        self.value = value
        self.start = start
        self.end = end
        self.type = "WalrusVarAssign"

    def __repr__(self):
        return f"{self.name} := {self.value}"


class OutNode(Node):
    def __init__(self, child, start, end):
        self.child = child
        self.start = start
        self.end = end
        self.type = "Out"

    def __repr__(self):
        return f"output {self.child}"


class IfNode(Node):
    def __init__(self, cond, children, else_children, start, end):
        self.cond = cond
        self.children = children
        self.else_children = else_children
        self.start = start
        self.end = end
        self.type = "If"

    def __repr__(self):
        return f"if {self.cond} do {self.children} else do {self.else_children}"


class OperationNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        self.start = self.left.start
        self.end = self.right.end
        self.type = "Operation"

    def __repr__(self):
        return f"({self.left} {self.op.value} {self.right})"


class ComparisonNode(Node):
    def __init__(self, left, comp, right):
        self.left = left
        self.comp = comp
        self.right = right
        self.start = self.left.start
        self.end = self.right.end
        self.type = "Comparison"

    def __repr__(self):
        return f"({self.left} {self.comp.value} {self.right})"


class CompListNode(Node):
    def __init__(self, children):
        self.children = children
        self.start = self.children[0].start
        self.end = self.children[-1].end
        self.type = "CompList"

    def __repr__(self):
        return f"{' '.join(map(repr, self.children))}"
