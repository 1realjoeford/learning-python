def average(numbers):
    sum_of_numbers = 0
    number_of_numbers = 0
    for number in numbers:
        if number.isdigit() :
            sum_of_numbers += int(number)
            number_of_numbers += 1
    result = sum_of_numbers / number_of_numbers
    return f'The average of the numbers is {result}'



print(average(input('Give a list of numbers> ')))



