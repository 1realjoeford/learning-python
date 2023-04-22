'''
weight_in_lb =input('How much do you weigh in pounds? ')
weight_in_kg = 0.453592 * float(weight_in_lb)
weight_in_kg = str(weight_in_kg)
print('You weigh ' + weight_in_kg + 'Kg ')
'''

weight = input('What is your weight?')
unit = input('(L)bs or (K)g ? ')
if unit.lower() == 'l':
    weight = 0.45 * int(weight)
    print(f'You weigh {weight}Kg')
elif unit.lower() == 'k':
    weight = int(weight) / 0.45
    print(f'You weigh {weight}lbs')