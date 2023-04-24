numbers = {
    '0' : 'zero',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven'
}

phone = 54335905761
phone_in_words = ''
for number in str(phone):
    phone_in_words += numbers.get(number, '!') + ' '

print(phone_in_words)
