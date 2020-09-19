from core.lexer.lexer import Lexer
from core.errors.pointer import point

file = "test.snow"

with open(file, "r") as f:
    code = f.read()

lexer = Lexer(code)
res = lexer.lex()
tokens, error = res

if error:
    print(point(code, error.pos))
    print(f"<{file}> " + repr(error))

else:
    print("\n".join(map(repr, tokens)))
