from abc import ABC, abstractmethod
class Account(ABC):
    
    def __init__(self, username: str, password: str, name: str, age: int) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.name = name.title()
        self.age = age
    
    def display(self):
        pass