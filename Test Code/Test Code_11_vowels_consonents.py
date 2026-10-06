import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("vowels", "Code/11_vowels_consonants.py").load_module()

assert program.count_vowels_consonants("Hello") == (2, 3)
assert program.count_vowels_consonants("Python") == (1, 5)

print("Test 11 passed")