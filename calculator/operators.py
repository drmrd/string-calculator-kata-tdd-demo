def add(numbers):
    if not numbers:
        return 0

    numbers = numbers.replace('\n', ',').split(',')
    return sum(int(number) for number in numbers)