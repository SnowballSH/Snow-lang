from core.compiler.compiler import run
from app import app
from timeit import timeit

# print(timeit(lambda: run("test.snow"), number=10))

app.run("test.snow")
