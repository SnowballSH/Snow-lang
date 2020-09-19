from .types import *
from ..errors.error import *

import os
d = os.getcwd()

stdout = open(f"{d}\\snow.stdout", "w")

stderr = open(f"{d}\\snow.stderr", "w")


class Interpreter:
    def __init__(self, nodes):
        self.nodes = nodes

    def run(self):
        res = None
        for node in self.nodes:
            res, e = self.visit(node)
            if e:
                return None, e

        return res, None

    def visit(self, node):
        """
        visit a node
        :param node: a node
        :return: (value, error)
        """
        if node.type == "Out":
            res, e = self.visit(node.child)
            if e:
                return None, e
            print(res.value, file=stdout)
            return None, None

        if node.type == "Number":
            return Number(node.value, node.start, node.end), None

        if node.type == "Operation":
            op = node.op
            left, e = self.visit(node.left)
            if e:
                return None, e
            right, e = self.visit(node.right)
            if e:
                return None, e

            if op.type == "ADD":
                if isinstance(left.value, (int, float)) and isinstance(right.value, (int, float)):
                    return Number(left.value + right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for +: {left.type} and {right.type}")

            if op.type == "MIN":
                if isinstance(left.value, (int, float)) and isinstance(right.value, (int, float)):
                    return Number(left.value - right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for -: {left.type} and {right.type}")

            if op.type == "MUL":
                if isinstance(left.value, (int, float)) and isinstance(right.value, (int, float)):
                    return Number(left.value * right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for *: {left.type} and {right.type}")

            if op.type == "DIV":
                if isinstance(left.value, (int, float)) and isinstance(right.value, (int, float)):
                    return Number(left.value / right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for /: {left.type} and {right.type}")

        raise Exception(f"BROKEN: {node}")
