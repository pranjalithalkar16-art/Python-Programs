def remove_duplicates(numbers):
    return list(set(numbers))


# Example
numbers = [1, 2, 2, 3, 4, 4, 5]
print("Original List:", numbers)
print("List after removing duplicates:", remove_duplicates(numbers))