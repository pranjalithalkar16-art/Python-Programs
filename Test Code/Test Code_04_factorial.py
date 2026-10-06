import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("factorial", "Code/04_factorial.py").load_module()

assert program.factorial(5) == 120
assert program.factorial(4) == 24
assert program.factorial(0) == 1

print("Test 4 passed")