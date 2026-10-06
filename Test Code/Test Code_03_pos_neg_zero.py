import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("pos_neg", "Code/03_pos_neg_zero.py").load_module()

assert program.check_number(10) == "Positive"
assert program.check_number(-5) == "Negative"
assert program.check_number(0) == "Zero"

print("Test 3 passed")