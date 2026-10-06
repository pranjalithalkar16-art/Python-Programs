import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("second_largest", "Code/15_second_largest.py").load_module()

assert program.second_largest([10, 20, 30, 40]) == 30
assert program.second_largest([5, 9, 2, 7]) == 7
assert program.second_largest([10, 10, 5, 8]) == 8

print("Test 15 passed")