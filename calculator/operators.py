def add(numbers):
    if numbers:
        numbers = numbers.split(',')
        if len(numbers) > 2:
            raise ValueError('add expects at most two integers in its input string')
        result = 0
        for number in numbers:
            result += int(number)
        return result

    return 0