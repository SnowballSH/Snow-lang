from core.compiler.compiler import run
from timeit import timeit

print(timeit(lambda: run("test.snow"), number=10))
