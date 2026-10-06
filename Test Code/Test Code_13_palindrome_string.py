import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("palindrome_string", "Code/13_palindrome_string.py").load_module()

assert program.is_palindrome("madam") == True
assert program.is_palindrome("hello") == False
assert program.is_palindrome("level") == True

print("Test 13 passed")