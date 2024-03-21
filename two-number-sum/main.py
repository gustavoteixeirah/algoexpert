array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

found = False
for number in array:
    for next in array:
        if number == next:
            continue
        if number + next == targetSum:
            print([number, next])
            found = True
            break
    if found:
        break
