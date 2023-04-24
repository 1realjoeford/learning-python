list = [1,2,5,7,5,2,5,7,9,5,1,6]
unique_list = []

for number in list:
    if number not in unique_list:
        unique_list.append(number)
print(unique_list)

