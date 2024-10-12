# class Person:
#     def__init__(self, dni, name, age)
#         self.__dni = dni
#         self.__name = __name
#         self.age = agregar

#     def __str__(self):
#         return f"Person(name={self.__name}), age={self.age})"


# person_1 = Person(1234, 'Luis', 20)
# print(person_1)

class ProductInventory:
    def __init__(self, product,saldo):
        self.product = product
        self.__stock = 0
    
    def add_stock(self,quantity):
        self.__stock += quantity

    def remove_stock(self,quantity)
        if quantity <= self.__stock
            self.__stock -= quantity
    
    def show_stock(self):
        return f"Para el producto {self.product} hay un stock de {self.stock}"

inventory = ProductInventory("Coca-cola") 
inventory.add_stock(100)
inventory.remove_stock(20)

inventory.__stock = 100

print(inventory.show_stock())

