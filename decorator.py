from abc import ABC, abstractmethod

class BasePizza(ABC):
    @abstractmethod
    def cost (self):
        pass 

class Margherita(BasePizza):
    def cost(self):
        return 100
    
class FarmHouse(BasePizza):
    def cost(self):
        return 150
    
class FarmHouse(BasePizza):
    def cost(self):
        return 200
    

class topping(BasePizza, ABC):

    def __init__(self,pizza):
        self.pizza = pizza 

    @abstractmethod
    def cost(self):
        pass

class cheese(topping):

    def cost(self):
        return self.pizza.cost() + 30 
    
class olives(topping):

    def cost(self):
        return self.pizza.cost() + 25


class capsicum(topping):

    def cost(self):
        return self.pizza.cost() + 10
    

if __name__ == "__main__":
    pizza = Margherita()
    print("Base Pizza Cost: ", pizza.cost())

    pizza2 = FarmHouse()
    pizza2 = cheese(pizza2)
    pizza2 = olives(pizza2)
    print("Pizza with toppings cost: ", pizza2.cost())

    pizza3 = FarmHouse()
    pizza3 = cheese(pizza3)
    pizza3 = olives(pizza3)
    pizza3 = capsicum(pizza3)
    print("Pizza with toppings cost: ", pizza3.cost())



'''Sometimes, instead of creating hundreds of subclasses for every pizza variation (e.g., Margherita + Cheese + Olive + Jalapeno), we use decorators.
his allows us to dynamically add toppings to pizzas at runtime.'''

'''This approach is more flexible and adheres to the Open/Closed Principle, as we can add new toppings without modifying existing code.'''