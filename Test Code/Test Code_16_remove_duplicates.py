import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader(
    "remove_duplicates",
    "Code/16_remove_duplicates.py"
).load_module()

assert program.remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
assert program.remove_duplicates([1, 1, 1]) == [1]
assert program.remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert program.remove_duplicates([]) == []

print("All test cases passed!")