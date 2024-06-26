def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
result = binarySearch(array, target)
print(result)
