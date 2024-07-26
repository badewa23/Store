from Account import Account
from User import User 
from Admin import Admin

class Person:
    def __init__(self, name: str, age: int, salary: float = None):
        self.name = name.title()
        self.age = age
        self.salary = salary
    
    def add_salary(self, ammount: float) -> None:
        self.salary += ammount