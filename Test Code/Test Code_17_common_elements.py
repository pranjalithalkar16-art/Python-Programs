import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("common", "Code/17_common_elements.py").load_module()

assert program.common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
assert program.common_elements([1, 2], [3, 4]) == []
assert program.common_elements([1, 2, 2], [2, 3]) == [2]

print("Test 17 passed")