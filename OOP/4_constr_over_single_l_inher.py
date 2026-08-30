class Product:
    def __init__(self, product_name, product_type):
        self.product_name = product_name
        self.product_type = product_type

class Item(Product):
    def __init__(self, product_name, product_type, quantity):
        # Calling parent constructor
        super().__init__(product_name, product_type)
        self.quantity = quantity

    def display(self):
        print("Product Name:", self.product_name)
        print("Product Type:", self.product_type)
        print("Quantity:", self.quantity)

# Object
obj = Item("Laptop", "Electronics", 5)
obj.display()
