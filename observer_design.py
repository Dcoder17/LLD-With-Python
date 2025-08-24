from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


class EmailNotification(Observer):
    def __init__(self, user_email: str):
        self.user_email = user_email

    def update(self, message: str):
        print(f"Email sent to {self.user_email}: {message}")


class PhoneNotification(Observer):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def update(self, message: str):
        print(f"SMS sent to {self.phone_number}: {message}")

class Product:
    def __init__(self, name: str):
        self.name = name
        self._observers = []  

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, message: str):
        for observer in self._observers:
            observer.update(message)

    def set_discount(self, percent: int):
        self.notify_observers(f"{self.name} is now {percent}% off!")


if __name__ == "__main__":
    product = Product("Laptop")

    email_observer = EmailNotification("yas1133@gmail.com")
    phone_observer = PhoneNotification("+1234567890")
    product.add_observer(email_observer)
    product.add_observer(phone_observer)
    product.set_discount(20) 
    product.remove_observer(phone_observer)
    product.set_discount(30)


'''
The Observer Pattern is a behavioral design pattern 
where an object (called Subject/Publisher) maintains a list of dependents (Observers/Subscribers) and automatically notifies them of any state changes.
'''
