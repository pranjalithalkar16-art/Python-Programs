import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("fibonacci", "Code/05_fibonacci_series.py").load_module()

assert program.fibonacci(5) == [0, 1, 1, 2, 3]
assert program.fibonacci(3) == [0, 1, 1]
assert program.fibonacci(1) == [0]

print("Test 5 passed")