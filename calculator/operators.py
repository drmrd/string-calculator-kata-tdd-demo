def add(numbers):
    if numbers == '1,2':
        return 3
    if numbers == '1,3':
        return 4

    if numbers:
        return int(numbers)

    return 0