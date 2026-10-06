import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader(
    "even_odd",
    "Code/01_even_odd.py"
).load_module()

assert program.check_even_odd(10) == "Even"
assert program.check_even_odd(13) == "odd"
assert program.check_even_odd(0) == "Even"

print("Test 1 passed")