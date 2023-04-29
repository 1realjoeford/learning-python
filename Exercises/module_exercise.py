import utils
from utils import find_least_number

numbers = [1, 13, 9, 5, 4, 9, 6]
print(utils.find_max_number(numbers))


numbers = [-2, 17, -7, 65, -91, 65, -23, 80, 9, -43]
least_number = find_least_number(numbers)
print(least_number)