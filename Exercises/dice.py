import random


class Dice:
    def roll(self):
        result = []
        for each in range(2):
            result.append(random.randint(1, 6))
        return tuple(result)
    

dice = Dice()
print(dice.roll())
        
