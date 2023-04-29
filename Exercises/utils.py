
def find_max_number(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


def find_least_number(numbers):
    least_number = numbers[0]
    for number in numbers:
        if number < least_number:
            least_number = number
    return least_number