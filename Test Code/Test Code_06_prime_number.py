import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("prime", "Code/06_prime_number.py").load_module()

assert program.is_prime(7) == True
assert program.is_prime(10) == False
assert program.is_prime(2) == True

print("Test 6 passed")