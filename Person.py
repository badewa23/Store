from Account import Account
from User import User 
from Admin import Admin

class Person:
    def __init__(self, name: str, age: int):
        self.name = name.title()
        self.age = age
        self.accounts = list()
    
    def add_account(self, account: Account) -> None:
        self.accounts.append(account)
    
    def delete_account(self, account: Account) -> bool:
        try:
            self.accounts.remove(account)
            return True
        except:
            return False
            
    
    def get_name(self):
        return self.name
    
    def add_salary(self, ammount: float) -> None:
        self.salary = float(ammount)
    
    def get_dictionary_info(self):
        try:
            return {"Name":self.name, "Age": self.age, "Salary": self.salary}
        except:
            return {"Name":self.name, "Age": self.age}