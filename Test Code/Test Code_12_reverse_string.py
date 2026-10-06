import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("reverse_string", "Code/12_reverse_string.py").load_module()

assert program.reverse_string("Hello") == "olleH"
assert program.reverse_string("Python") == "nohtyP"
assert program.reverse_string("abc") == "cba"

print("Test 12 passed")