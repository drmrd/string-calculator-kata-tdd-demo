def add(numbers):
    if numbers:
        numbers = numbers.split(',')
        result = 0
        for number in numbers:
            result += int(number)
        return result

    return 0