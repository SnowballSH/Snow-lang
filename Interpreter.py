from all_types import *
from copy import deepcopy

from libs import lib


class UndefinedError(Exception):
    pass


def is_num(left=0, right=0):
    return type(left) in [float, int] and type(right) in [float, int]


class Interpreter:
    def __init__(self):
        self.tree = {}
        self.import_package("types")

    def run(self, nodes):
        for n in nodes:
            a = self.visit(n)
            if type(n).__name__ == "GiveNode":
                return a
        return

    def import_package(self, name):
        try:
            package = lib.get[name]
        except KeyError:
            raise ImportError(f"Package not found: {name}")

        for m in package:
            self.tree.update({m[0]: PythonFunction(m[0], m[1], m[2])})

    def visit(self, node):
        type_ = type(node).__name__
        if type_ == "ImportNode":
            self.import_package(node.package[1])
            return

        if type_ == "PutNode":
            expr = self.visit(node.expr)
            print(expr)
            return

        if type_ == "GetNode":
            x = input(self.visit(node.expr))
            return String(x)

        if type_ == "IfNode":
            cond, then, else_, mode = vars(node).values()
            ans = Null()
            if self.visit(cond).value:
                for a in then:
                    ans = self.visit(a)
            else:
                if else_ is not None:
                    for a in else_:
                        ans = self.visit(a)
            return ans if mode == "?" else None

        if type_ == "ForNode":
            var, stop, action, body = vars(node).values()
            self.visit(var)
            while self.visit(stop).value:
                for b in body:
                    self.visit(b)
                self.visit(action)

            return

        if type_ == "VarAssignNode":
            value = node.value
            value = self.visit(value)
            self.tree.update({node.name[1]: value})
            return

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
            return

        if type_ == "AnonFuncAssignNode":
            name = node.name
            paras = node.parameters
            call = node.call
            return Function(name, paras, call)

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
                c = inter.run(func.call)
                return c

            new = [self.visit(p) for p in pars]
            return func.call(*new)

        if type_ == "GiveNode":
            expr = node.expr
            return self.visit(expr)

        if type_ == "NumberNode":
            return Number(node.value)

        if type_ == "StringNode":
            return String(node.value)

        if type_ == "BoolNode":
            return Boolean(node.value)

        if type_ == "NullNode":
            return Null()

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
                if is_num(left, right):
                    return Number(left + right)
                if type(left) == type(right) == str:
                    return String(left + right)
                raise TypeError(f"unsupported operand type(s) for +: {type(left).__name__} and {type(right).__name__}")
            if op == "-":
                if is_num(left, right):
                    return Number(left - right)
                raise TypeError(f"unsupported operand type(s) for -: {type(left).__name__} and {type(right).__name__}")
            if op == "*":
                if is_num(left, right):
                    return Number(left * right)
                raise TypeError(f"unsupported operand type(s) for *: {type(left).__name__} and {type(right).__name__}")
            if op == "/":
                if is_num(left, right):
                    return Number(left / right)
                raise TypeError(f"unsupported operand type(s) for /: {type(left).__name__} and {type(right).__name__}")
            raise Exception("broken")

        if type_ == "UnaryOpNode":
            op = node.op[1]
            right = self.visit(node.right).value
            if op == "+":
                if is_num(right=right):
                    return Number(+ right)
                raise TypeError(f"unsupported operand type for unary +: {type(right).__name__}")
            if op == "-":
                if is_num(right=right):
                    return Number(- right)
                raise TypeError(f"unsupported operand type for unary -: {type(right).__name__}")
            if op == "!":
                return Boolean(int(not right))
            else:
                raise Exception("broken")
        raise Exception("broken")
