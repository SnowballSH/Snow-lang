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


class IdentifierNode(Node):
    def __init__(self, value, start, end):
        self.value = value
        self.start = start
        self.end = end
        self.type = "Identifier"

    def __repr__(self):
        return f"{self.value}"


class OutNode(Node):
    def __init__(self, child, start, end):
        self.child = child
        self.start = start
        self.end = end
        self.type = "Out"

    def __repr__(self):
        return f"output {self.child}"


class OperationNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        self.start = self.left.start
        self.end = self.right.end
        self.type = "Operation"

    def __repr__(self):
        return f"({self.left} {self.op.type} {self.right})"
