from all_types import *
from copy import deepcopy

from libs import lib


class UndefinedError(Exception):
    pass


class Interpreter:
    def __init__(self):
        self.tree = {}

    def run(self, nodes):
        for n in nodes:
            self.visit(n)

    def visit(self, node):
        type_ = type(node).__name__
        if type_ == "ImportNode":
            try:
                package = lib.get[node.package[1]]
            except ImportError:
                raise ImportError(f"Package not found: {node.package[1]}")

            for m in package:
                self.tree.update({m[0]: PythonFunction(m[0], m[1], m[2])})

            return Number(float("nan"))

        if type_ == "PutNode":
            print(self.visit(node.expr))
            return Number(float("nan"))

        if type_ == "GetNode":
            x = input(self.visit(node.expr))
            return String(x)

        if type_ == "VarAssignNode":
            value = node.value
            value = self.visit(value)
            self.tree.update({node.name[1]: value})
            return Number(float("nan"))

        if type_ == "VarAccessNode":
            name = node.name[1]
            if name not in self.tree:
                raise UndefinedError(f"'{name}' is not defined")
            value = self.tree[name]
            return value

        if type_ == "FuncAssignNode":
            name = node.name
            paras = node.parameters
            call = node.call
            self.tree.update({node.name[1]: Function(name, paras, call)})
            return Number(float("nan"))

        if type_ == "FuncAccessNode":
            name = node.name[1]
            if name not in self.tree:
                raise UndefinedError(f"'{name}' is not defined")
            pars = node.parameters
            func = self.tree[name]
            if func.type not in ["func", "py_func"]:
                raise RuntimeError(f"type '{func.type}' is not callable")
            if func.type == "func":
                inter = Interpreter()
                inter.tree = deepcopy(self.tree)
                for i, p in enumerate(pars):
                    inter.tree.update({func.parameters[i][1]: self.visit(p)})
                return inter.run(func.call)

            new = [self.visit(p) for p in pars]
            return func.call(*new)

        if type_ == "NumberNode":
            return Number(node.value)

        if type_ == "StringNode":
            return String(node.value)

        if type_ == "CompNode":
            left = self.visit(node.left).value
            right = self.visit(node.right).value
            if node.op[1] == "==":
                return Boolean(int(left == right))
            if node.op[1] == "!=":
                return Boolean(int(left != right))
            if node.op[1] == ">":
                return Boolean(int(left > right))
            if node.op[1] == "<":
                return Boolean(int(left < right))
            if node.op[1] == ">=":
                return Boolean(int(left >= right))
            if node.op[1] == "<=":
                return Boolean(int(left <= right))

        if type_ == "OpNode":
            left = self.visit(node.left).value
            right = self.visit(node.right).value
            op = node.op[1]
            if op == "+":
                if type(left) == type(right) == int:
                    return Number(left + right)
                if type(left) == type(right) == str:
                    return String(left + right)
                raise TypeError(f"unsupported operand type(s) for +: {type(left).__name__} and {type(right).__name__}")
            if op == "-":
                if type(left) == type(right) == int:
                    return Number(left - right)
                raise TypeError(f"unsupported operand type(s) for -: {type(left).__name__} and {type(right).__name__}")
            if op == "*":
                if type(left) == type(right) == int:
                    return Number(left * right)
                raise TypeError(f"unsupported operand type(s) for *: {type(left).__name__} and {type(right).__name__}")
            if op == "/":
                if type(left) == type(right) == int:
                    return Number(left / right)
                raise TypeError(f"unsupported operand type(s) for /: {type(left).__name__} and {type(right).__name__}")
            raise Exception("broken")

        if type_ == "UnaryOpNode":
            op = node.op[1]
            right = self.visit(node.right).value
            if op == "+":
                if type(right) == int:
                    return Number(+ right)
                raise TypeError(f"unsupported operand type for unary +: {type(right).__name__}")
            if op == "-":
                if type(right) == int:
                    return Number(- right)
                raise TypeError(f"unsupported operand type for unary -: {type(right).__name__}")
            if op == "!":
                return Boolean(int(not right))
            else:
                raise Exception("broken")
        raise Exception("broken")
