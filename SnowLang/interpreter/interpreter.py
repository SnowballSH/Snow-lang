from __future__ import print_function

from .types import *
from ..errors.error import *
from ..parser.nodes import *

from ..lexer.lexer import Lexer
from ..parser.parser import Parser

import os
import sys

sys.setrecursionlimit(10 ** 5)
d = os.getcwd()


class Interpreter:
    def __init__(self, nodes, stdout, tree=None, depth=0):
        if tree is None:
            self.tree = {}
        else:
            self.tree = tree
        self.builtin = {"Void": lambda *a: Void(*a), "True": lambda *a: Bool(True, *a),
                        "False": lambda *a: Bool(False, *a)}
        self.stdout = stdout
        self.nodes = nodes
        self.depth = depth

        self.to_break = False
        self.to_return = False

    def run(self):
        for node in self.nodes:
            res, e = self.visit(node)
            if e:
                return None, e

            if self.to_return:
                to_return = self.to_return
                self.to_return = None
                return to_return, None

        return None, None

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

            value = res.value

            print(value, file=self.stdout)

            return Void(node.start, res.end), None

        if node.type == "If":
            cond, children, else_children = node.cond, node.children, node.else_children
            cond, e = self.visit(cond)
            if e:
                return None, e

            if cond.value:
                for child in children:
                    res, e = self.visit(child)
                    if e:
                        return None, e

            elif else_children is not None:
                for child in else_children:
                    res, e = self.visit(child)
                    if e:
                        return None, e

            return Void(node.start, node.end), None

        if node.type == "Loop":
            while True:
                for child in node.children:
                    res, e = self.visit(child)
                    if e:
                        return None, e
                    if self.to_break:
                        break

                if self.to_break:
                    self.to_break = False
                    break

            return Void(node.start, node.end), None

        if node.type == "Repeat":
            times, e = self.visit(node.times)
            if e:
                return None, e

            times = times.value
            if type(times) is not int:
                return None, SnowError.TypeError(node.times.start, f"Expected type integer Number, got '{times}'")

            for i in range(times):
                if node.as_ is not None:
                    new_node = VarAssignNode(node.as_, Number(i, node.start, node.end), node.times.end, node.end)
                    _, e = self.visit(new_node)
                    if e:
                        return None, e

                for child in node.children:
                    res, e = self.visit(child)
                    if e:
                        return None, e
                    if self.to_break:
                        break

                if self.to_break:
                    self.to_break = False
                    break

            return Void(node.start, node.end), None

        if node.type == "Break":
            self.to_break = True
            return Void(node.start, node.end), None

        if node.type == "Return":
            if self.to_return is None:
                return None, SnowError.SyntaxError(node.start, "return outside function")
            self.to_return, e = self.visit(node.child)
            if e:
                return None, e
            return Void(node.start, node.end), None

        if node.type == "Include":
            try:
                with open(f"{os.path.dirname(__file__)}/../library/{node.name}.snow") as f:
                    code = f.read()
            except FileNotFoundError:
                return None, SnowError.ModuleNotFoundError(node.start, node.name)

            def raise_e():
                print(f"Error found in <{node.name}>:\n{repr(e)}\n")
                return None, SnowError.ModuleError(node.start)

            lexer = Lexer(code)
            res = lexer.lex()
            tokens, e = res
            if e:
                return raise_e()

            parser = Parser(tokens)
            res = parser.parse()
            nodes, e = res
            if e:
                return raise_e()

            inter = Interpreter(nodes, self.stdout)
            res, e = inter.run()
            if e:
                return raise_e()

            self.tree.update(inter.tree)

            return Void(node.start, node.end), None

        if node.type == "FuncAssign":
            name, args, body = node.name, node.args, node.body

            if node.name in self.builtin.keys():
                return None, SnowError.OverrideError(node.start, f"Cannot override builtin: '{node.name}'")

            self.tree[node.name] = Function(node.start, node.end, name, args, body)
            return Void(node.start, node.end), None

        if node.type == "FuncAccess":
            if node.name in self.tree:
                func = self.tree[node.name]
                if not func.callable:
                    return None, SnowError.NotCallableError(node.start, func.type)

                body = func.body
                tree = {}
                tree.update(self.tree)

                if len(node.args) > len(func.args):
                    return None, SnowError.ArgumentError(node.args[len(func.args)].start, "unexpected argument(s)")
                if len(node.args) < len(func.args):
                    return None, SnowError.ArgumentError(node.args[-1].end, "too less argument(s)")

                args = []
                to_return = Void(node.start, node.end)
                for a in node.args:
                    res, e = self.visit(a)
                    if e:
                        return None, e
                    args.append(res)

                tree.update([*zip(func.args, args)])
                inter = Interpreter(body, self.stdout, tree=tree, depth=self.depth + 1)
                res, e = inter.run()
                if e:
                    return None, e

                if res is not None:
                    to_return = res

                return to_return, None

            elif node.name in self.builtin:
                func: Function = self.builtin[node.name]
                if not func.callable:
                    return None, SnowError.NotCallableError(node.start, func.type)
                body = func.body
                tree = {}
                tree.update(self.tree)
                if len(node.args) > len(func.args):
                    return None, SnowError.ArgumentError(node.args[len(func.args)].start, "unexpected argument(s)")
                if len(node.args) < len(func.args):
                    return None, SnowError.ArgumentError(node.args[-1].end, "too less argument(s)")
                args = []
                to_return = Void(node.start, node.end)
                for a in node.args:
                    res, e = self.visit(a)
                    if e:
                        return None, e
                    args.append(res)
                tree.update([*zip(func.args, args)])
                inter = Interpreter(body, self.stdout, tree=tree, depth=self.depth + 1)
                res, e = inter.run()
                if e:
                    return None, e
                if res is not None:
                    to_return = res
                return to_return, None

            else:
                return None, SnowError.UndefinedError(node.start, node.name)

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

        if node.type == "Comparison":
            left, comp, right = self.visit(node.left), node.comp, self.visit(node.right)
            left, e = left
            if e:
                return None, e
            right, e = right
            if e:
                return None, e

            try:
                if comp.type == "DBEQ":
                    return Bool(left.value == right.value, left.start, right.end), None
                if comp.type == "NOTEQ":
                    return Bool(left.value != right.value, left.start, right.end), None
                if comp.type == "LT":
                    return Bool(left.value < right.value, left.start, right.end), None
                if comp.type == "GT":
                    return Bool(left.value > right.value, left.start, right.end), None
                if comp.type == "LTEQ":
                    return Bool(left.value <= right.value, left.start, right.end), None
                if comp.type == "GTEQ":
                    return Bool(left.value >= right.value, left.start, right.end), None
            except TypeError:
                return None, SnowError.TypeError(comp.start, f"Cannot use '{comp.value}' between type "
                                                             f"'{left.type}' and '{right.type}'")

        if node.type == "CompList":
            children = node.children
            for child in children:
                res, e = self.visit(child)
                if e:
                    return None, e

                if res.value is True:
                    return Bool(True, node.start, node.end), None
            return Bool(False, node.start, node.end), None

        if node.type == "Operation":
            op = node.op
            left, e = self.visit(node.left)
            if e:
                return None, e
            right, e = self.visit(node.right)
            if e:
                return None, e

            can_op = lambda n: isinstance(n, (Number, Bool))

            if op.type == "ADD":
                if can_op(left) and can_op(right):
                    return Number(left.value + right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for +: {left.type} and {right.type}")

            if op.type == "MIN":
                if can_op(left) and can_op(right):
                    return Number(left.value - right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for -: {left.type} and {right.type}")

            if op.type == "MUL":
                if can_op(left) and can_op(right):
                    return Number(left.value * right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for *: {left.type} and {right.type}")

            if op.type == "DIV":
                if can_op(left) and can_op(right):
                    if right.value == 0:
                        return None, SnowError.ZeroDivisionError(right.start)
                    return Number(left.value / right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for /: {left.type} and {right.type}")

            if op.type == "INTDIV":
                if can_op(left) and can_op(right):
                    if right.value == 0:
                        return None, SnowError.ZeroDivisionError(right.start)
                    return Number(left.value // right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for //: {left.type} and {right.type}")

            if op.type == "MOD":
                if can_op(left) and can_op(right):
                    return Number(left.value % right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for %: {left.type} and {right.type}")

            if op.type == "POW":
                if can_op(left) and can_op(right):
                    return Number(left.value ** right.value, left.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type(s) for ^: {left.type} and {right.type}")

        if node.type == "UnaryOp":
            op = node.op
            right, e = self.visit(node.right)
            if e:
                return None, e

            can_op = lambda n: isinstance(n, (Number, Bool))

            if op.type == "ADD":
                if can_op(right):
                    return Number(right.value, op.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type for unary +: {right.type}")

            if op.type == "MIN":
                if can_op(right):
                    return Number(- right.value, op.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type for unary -: {right.type}")

            if op.type == "NOT":
                if can_op(right):
                    return Bool(not right.value, op.start, right.end), None
                return None, SnowError.TypeError(op.start,
                                                 f"unsupported operand type for unary !: {right.type}")

        raise Exception(f"BROKEN: {node}")
