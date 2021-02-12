def add(numbers):
    if numbers:
        return sum(int(number) for number in numbers.split(','))
    return 0