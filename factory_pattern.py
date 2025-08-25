from abc import ABC, abstractmethod 

class notification(ABC):
    @abstractmethod
    def send(self):
        pass

class EmailNotification(notification):
    def send(self):
        print("Sending Email Notification")

class SMSNotification(notification):
    def send(self):
        print("Sending SMS Notification")

class pushNotification(notification):
    def send(self):
        print("Sending Push Notification")

class NotificationFactory:
    @staticmethod
    def get_notification(method: str) -> notification:
        if method == "email":
            return EmailNotification()
        elif method == "sms":
            return SMSNotification()
        elif method == "push":
            return pushNotification()
        else:
            raise ValueError(f"Unknown notification method: {method}")
        

if __name__ == "__main__":
    factory = NotificationFactory()
    notifier = factory.get_notification("EMAIL".lower())
    notifier.send()

    notifier = factory.get_notification("SMS".lower())
    notifier.send()
    notifier = factory.get_notification("PUSH".lower())
    notifier.send()


'''it manages too many classes and avoids tightly coupled object creation by keeping a centralized factory that returns objects based on input.'''
''' Loose coupling (client depends only on the interface, not concrete class).

Centralized object creation (easy to manage).

Easier to extend (just add a new class and update factory).
'''