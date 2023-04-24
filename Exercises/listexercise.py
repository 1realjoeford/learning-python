numbers = [1, 3, 17, 8, 45, 89, 63, 3]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number

print(largest_number)