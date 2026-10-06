import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("duplicates", "Code/19_find_duplicates.py").load_module()

assert program.find_duplicates([1, 2, 2, 3, 3, 4]) == [2, 3]
assert program.find_duplicates([1, 2, 3]) == []
assert program.find_duplicates([5, 5, 6, 6]) == [5, 6]

print("Test 19 passed")