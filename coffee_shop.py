from abc import ABC, abstractmethod

class CoffeBase(ABC):

    @abstractmethod
    def cost(self):
        pass 

    @abstractmethod
    def getDescription(self):
        pass 

class Espresso(CoffeBase):
    def cost(self):
        return 100
    
    def getDescription(self):
        return "Espresso"
    
class Latte(CoffeBase):
    def cost(self):
        return 150
    
    def getDescription(self):
        return "Latte"
    
class ExtraCompentent(CoffeBase, ABC):

    def __init__(self,coffee):
        self.coffee = coffee 

    @abstractmethod
    def cost(self):
        pass


class Milk(ExtraCompentent):
    def cost(self):
        return self.coffee.cost() + 20 
    
    def getDescription(self):
        return self.coffee.getDescription() + ", Milk"
    

class Sugar(ExtraCompentent):
    def cost(self):
        return self.coffee.cost() + 10 
    
    def getDescription(self):
        return self.coffee.getDescription() + ", Sugar"
    
class WhippedCream(ExtraCompentent):
    def cost(self):
        return self.coffee.cost() + 30 
    
    def getDescription(self):
        return self.coffee.getDescription() + ", Whipped Cream"
    

if __name__ == "__main__":
    BaseCoffee1 = Espresso()
    print("Total Coffee Cost:", BaseCoffee1.cost(), " Description:", BaseCoffee1.getDescription())

    Coffee2 = Latte()
    Coffee2 = Sugar(Coffee2)
    print("Total Coffee Cost:", Coffee2.cost(), " Description:", Coffee2.getDescription())

    Coffee2_with_Milk = Milk(Coffee2)
    print("Total Coffee Cost:", Coffee2_with_Milk.cost(), " Description:", Coffee2_with_Milk.getDescription())