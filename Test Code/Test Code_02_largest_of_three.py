import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("largest", "Code/02_largest_of_three.py").load_module()

assert program.largest(10, 25, 15) == 25
assert program.largest(50, 20, 30) == 50
assert program.largest(5, 8, 3) == 8

print("Test 2 passed")