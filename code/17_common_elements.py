def common_elements(list1, list2):
    result = []

    for item in list1:
        if item in list2 and item not in result:
            result.append(item)

    return result


print(common_elements([1, 2, 3], [2, 3, 4]))