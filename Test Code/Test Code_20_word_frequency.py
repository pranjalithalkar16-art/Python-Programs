import sys
sys.path.append("Code")

from importlib.machinery import SourceFileLoader

program = SourceFileLoader("word_frequency", "Code/20_word_frequency.py").load_module()

assert program.word_frequency("hello world hello") == {
    "hello": 2,
    "world": 1
}

assert program.word_frequency("python python code") == {
    "python": 2,
    "code": 1
}

print("Test 20 passed")