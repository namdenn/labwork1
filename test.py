import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity):
        
        assert price >= 0, f"price {price} is not greater than or equal to zero!"    
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero!"
        # print(f"An instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    # def calculate_total_price(self, x, y):
    #     return x * y
        
    def calculate_total_price(self):
        return self.quantity  * self.price
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity} )"


# item1 = Item("samsung", 100, 5)
# item1.apply_discount()
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = Item("laptop", 1000, 15)
# item2.price = 1000
# item2.quantity = 15
# print(item2.calculate_total_price(item2.price, item2.quantity))


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
# print(Item.all)

# for instance in Item.all:
#     print(instance.name)

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)

# print(item1.calculate_total_price())

# print(Item.__dict__)# All the attributes for Class level
# print(item1.__dict__)# All the attributes for instance level

# Item.instantiate_from_csv()

print(Item.is_integer(7))
