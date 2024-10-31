from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class BasicNotifier(Notifier):
    def send(self, message):
        print(f"Notificación: {message}")

class NotifierDecorator(Notifier):
    def __init__(self, notifier):
        self.notifier = notifier

    def send(self, message):
        self.notifier.send(message)

class EmailNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        self.send_email(message)

    def send_email(self, message):
        print(f"Enviando correo: {message}")

class SMSNotifier(NotifierDecorator):
    def send(self, message):
        super().send(message)
        self.send_sms(message)

    def send_sms(self, message):
        print(f"Enviando SMS: {message}")

# Uso de los decoradores
basic_notifier = BasicNotifier()               
email_notifier = EmailNotifier(basic_notifier) 
sms_notifier = SMSNotifier(basic_notifier)     

sms_notifier.send("Tu pedido ha sido enviado.")
email_notifier.send("Tu pedido se perdio")
