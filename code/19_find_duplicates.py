def find_duplicates(numbers):
    duplicates = []

    for num in numbers:
        if numbers.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    return duplicates


print(find_duplicates([1, 2, 2, 3, 3, 4]))