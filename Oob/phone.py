from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        #Call super function to have access to parent attributes and methods
        super().__init__(
            name, price, quantity
        )

        #Run validation to received arguments
        assert broken_phones >= 0, f" Broken phones {broken_phones} should be greater than or equal to zero"

        #Assign to self object
        self.broken_phones = broken_phones


itel1  = Phone('kofi', 40, 5, 12)
print(itel1.broken_phones)
