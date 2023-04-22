name = input('What is your name? ')
name_length = len(name)
if name_length < 3:
    print('Name must be at least 3 characters long')
elif name_length > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good')