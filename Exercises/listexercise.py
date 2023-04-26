numbers = input('Provide a list of numbers> ')
largest_number = numbers[0]
for number in numbers:
    if number.isdigit():
        if number > largest_number:
            largest_number = number

print(largest_number)