'''
def mean(numbers):
    sum_of_numbers = 0
    number_of_numbers = 0
    for number in numbers:
        if number.isdigit() :
            sum_of_numbers += int(number)
            number_of_numbers += 1
    result = sum_of_numbers / number_of_numbers
    return f'The mean of the numbers is {result}'



print(mean(input('Give a list of numbers> ')))
'''


def mean(numbers):
    numbers_list = numbers.split()
    sum_of_numbers = 0
    number_of_numbers = 0
    for number in numbers_list:
        print(number)
        if number.isdigit():
            print(number)
            sum_of_numbers += int(number)
            number_of_numbers += 1
    print(number_of_numbers)
    result = sum_of_numbers / number_of_numbers
    return f'The mean of the numbers is {result}'

input_numbers = input(str('Give a list of numbers> '))
print(mean(input_numbers))