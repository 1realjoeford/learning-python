'''
item1 = Item('phone', 100, 3)
item1.apply_discount()
print(item1.calculate_total_price())
#print(item1.__dict__) #prints the attributes for the instance level
#print(Item.__dict__) #prints the attributes for the class level


item2 = Item('laptop', 1000, 2)
item2.pay_rate = 0.9
item2.apply_discount()
print(item2.calculate_total_price())
'''