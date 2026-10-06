import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("reverse", "Code/08_reverse_number.py").load_module()

assert program.reverse_number(1234) == 4321
assert program.reverse_number(100) == 1
assert program.reverse_number(25) == 52

print("Test 8 passed")