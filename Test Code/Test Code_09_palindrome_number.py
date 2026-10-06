import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("palindrome_number", "Code/09_palindrome_number.py").load_module()

assert program.is_palindrome(121) == True
assert program.is_palindrome(123) == False
assert program.is_palindrome(1221) == True

print("Test 9 passed")