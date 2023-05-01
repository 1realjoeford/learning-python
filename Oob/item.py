import csv


class Item:
    pay_rate = 0.8 # rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        #Run validations to recieved arguments
        assert price >= 0, f"Price {price} has to be greater than zero"
        assert quantity >= 0, f"Quantity {quantity} has to be greater than zero"


        #Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to carry out
        Item.all.append(self)

    
    def calculate_total_price(self):
        return self.price * self.quantity
    

    def apply_discount(self):
        self.price = self.price * self.pay_rate


    @classmethod
    def instantiate_from_csv(self):
        with open('E:\joe\evideos\programming\python\learning python\Oob\items.csv', 'r') as file:
            items = csv.DictReader(file)
            items = list(items)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    

Item.instantiate_from_csv()