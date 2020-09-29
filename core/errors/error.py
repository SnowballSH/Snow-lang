class SnowError:
    class SyntaxError:
        def __init__(self, pos, message="Invalid Syntax"):
            self.message = message
            self.pos = pos

        def __repr__(self):
            return f"Syntax Error: {self.message} at line {self.pos[0]}, char {self.pos[1]}"

    class TypeError:
        def __init__(self, pos, message):
            self.message = message
            self.pos = pos

        def __repr__(self):
            return f"Type Error: {self.message} at line {self.pos[0]}, char {self.pos[1]}"

    class ZeroDivisionError:
        def __init__(self, pos):
            self.pos = pos

        def __repr__(self):
            return f"Zero Division Error: division by zero at line {self.pos[0]}, char {self.pos[1]}"

    class OverrideError:
        def __init__(self, pos, message):
            self.message = message
            self.pos = pos

        def __repr__(self):
            return f"Override Error: {self.message} at line {self.pos[0]}, char {self.pos[1]}"

    class UndefinedError:
        def __init__(self, pos, message):
            self.message = message
            self.pos = pos

        def __repr__(self):
            return f"Undefined Error: {self.message} is not defined at line {self.pos[0]}, char {self.pos[1]}"

    class ArgumentError:
        def __init__(self, pos, message):
            self.message = message
            self.pos = pos

        def __repr__(self):
            return f"Argument Error: {self.message} at line {self.pos[0]}, char {self.pos[1]}"

    class NotCallableError:
        def __init__(self, pos, message):
            self.message = message
            self.pos = pos

        def __repr__(self):
            return f"Not Callable Error: type '{self.message}' " \
                   f"is not callable at line {self.pos[0]}, char {self.pos[1]}"

    class InvalidCharError:
        def __init__(self, pos):
            self.message = "Invalid Character"
            self.pos = pos

        def __repr__(self):
            return f"Syntax Error: {self.message} at line {self.pos[0]}, char {self.pos[1]}"
