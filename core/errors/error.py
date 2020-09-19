class SnowError:
    class SyntaxError:
        def __init__(self, pos):
            self.message = "Invalid Syntax"
            self.pos = pos

        def __repr__(self):
            return f"Syntax Error: {self.message} at line {self.pos[0]}, char {self.pos[1]}"

    class InvalidCharError:
        def __init__(self, pos):
            self.message = "Invalid Character"
            self.pos = pos

        def __repr__(self):
            return f"Syntax Error: {self.message} at line {self.pos[0]}, char {self.pos[1]}"
