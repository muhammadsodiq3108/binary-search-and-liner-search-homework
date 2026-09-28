def binary_search(numbers, target):
    chap = 0
    ong = len(numbers) - 1

    while chap <= ong:
        orta = (chap + ong) // 2

        if numbers[orta] == target:
            return orta
        elif numbers[orta] < target:
            chap = orta + 1
        else:
            ong = orta - 1

    return False


numbers = [1, 3, 5, 7, 9, 11, 15]

print(binary_search(numbers, 7))
print(binary_search(numbers, 8))
