class SnowObject:
    def __init__(self):
        self.methods = []
        self.type = None
        self.value = None

    def __repr__(self):
        return "Object"


class Number(SnowObject):
    def __init__(self, value: any):
        super().__init__()
        self.type = "int"
        self.value = value

    def __repr__(self):
        return str(self.value)


class String(SnowObject):
    def __init__(self, value: str):
        super().__init__()
        self.type = "str"
        self.value = value

    def __repr__(self):
        return str(self.value)


class Boolean(Number):
    def __init__(self, value: any):
        super().__init__(int(value))
        self.type = "bool"

    def __repr__(self):
        return str(bool(self.value))


class Null(SnowObject):
    def __init__(self):
        super().__init__()
        self.value = None
        self.type = "null"

    def __repr__(self):
        return "Null"


class Function(SnowObject):
    def __init__(self, name, parameters, call):
        super().__init__()
        self.type = "func"
        self.name = name
        self.parameters = parameters
        self.call = call

    def __repr__(self):
        return f"function '{self.name[1]}'"


class PythonFunction(SnowObject):
    def __init__(self, name, parameters, call):
        super().__init__()
        self.type = "py_func"
        self.name = name
        self.parameters = parameters
        self.call = call

    def __repr__(self):
        return f"python function '{self.name[1]}'"
