import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("missing", "Code/18_missing_number.py").load_module()

assert program.missing_number([1, 2, 3, 5]) == 4
assert program.missing_number([1, 2, 4, 5]) == 3
assert program.missing_number([1, 2, 3, 4, 6]) == 5

print("Test 18 passed")