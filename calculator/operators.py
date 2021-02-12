def add(numbers):
    if not numbers:
        return 0

    numbers = numbers.split(',')
    if len(numbers) > 2:
        raise ValueError('add expects at most two integers in its input string')

    return sum(int(number) for number in numbers)