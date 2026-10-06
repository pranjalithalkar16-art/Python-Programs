import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("frequency", "Code/14_char_frequency.py").load_module()

assert program.char_frequency("hello") == {
    "h": 1,
    "e": 1,
    "l": 2,
    "o": 1
}

assert program.char_frequency("aaa") == {"a": 3}

print("Test 14 passed")