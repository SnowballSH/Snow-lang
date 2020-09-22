from __future__ import print_function

from .types import *
from ..errors.error import *

import os

d = os.getcwd()


class Interpreter:
    def __init__(self, nodes, stdout, tree=None):
        if tree is None:
            self.tree = {}
        self.builtin = {"Void": lambda *a: Void(*a)}
        self.stdout = stdout
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
            print(res.value, file=self.stdout)

            return Void(node.start, res.end), None

        if node.type == "VarAccess":
            if node.value in self.tree:
                return self.tree[node.value], None
            elif node.value in self.builtin:
                x = self.builtin[node.value]
                return x(node.start, node.end), None
            else:
                return None, SnowError.UndefinedError(node.start, node.value)

        if node.type == "VarAssign":
            res, e = self.visit(node.value)
            if e:
                return None, e
            if node.name in self.builtin.keys():
                return None, SnowError.OverrideError(node.start, f"Cannot override builtin: '{node.name}'")
            self.tree[node.name] = res
            return Void(node.start, node.end), None

        if node.type == "WalrusVarAssign":
            res, e = self.visit(node.value)
            if e:
                return None, e
            self.tree[node.name] = res
            return res, None

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
                if isinstance(left, Number) and isinstance(right, Number):
                    return Number(left.value + right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for +: {left.type} and {right.type}")

            if op.type == "MIN":
                if isinstance(left, Number) and isinstance(right, Number):
                    return Number(left.value - right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for -: {left.type} and {right.type}")

            if op.type == "MUL":
                if isinstance(left, Number) and isinstance(right, Number):
                    return Number(left.value * right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for *: {left.type} and {right.type}")

            if op.type == "DIV":
                if isinstance(left, Number) and isinstance(right, Number):
                    return Number(left.value / right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for /: {left.type} and {right.type}")

        raise Exception(f"BROKEN: {node}")
