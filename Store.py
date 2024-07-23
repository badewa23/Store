from Person import Person
from User import User
from Admin import Admin
from Account import Account
from Item import Item

class Store:

    def __init__(self, name: str):
        self.name: str = name.title()
        self.inventory: list = list()
        self.accounts: list = list()
        self.persons: list = list()
    
    def item_name_exist(self, item_name: str) -> bool:
        for item in self.inventory:
            if item_name.capitalize() == item.get_item_name():
                return True
        return False
    
    def add_item(self, item_name:str, price:float, in_stock: int) -> Item:
        if self.item_name_exist(item_name):
            return None
        item = Item(item_name, price, in_stock)
        self.inventory.append(item)
        return self.inventory[-1]
    
    def remove_item(self, item: Item) -> bool:
        try:
            self.inventory.remove(item)
            return True
        except:
            return False
            
    def username_exist(self, username: str) -> bool:
        for account in self.accounts:
            if username == account.get_username():
                return True
        return False
    
    def check_if_pesron_exist(self, name:str) -> Person:
        name = name.title()
        for person in self.persons:
            if person.get_name() == name:
                return person
        return None
    
    def create_account_from_person(self, username:str, password:str, privilege: bool, name: str) -> Account:
        account: Account
        person: Person = self.check_if_pesron_exist(name)
        if person is not None:
            if privilege:
                account = self.create_admin(username, password,name)
            else:
                account = self.create_user(username, password,name)
            if account is not None:
                person.add_account(account)
            return account
        return None
    
    def create_account(self, username: str, password: str, privilege: bool, name: str, age:int) -> Account:
        account: Account
        person = Person(name, age)
        if privilege:
            account = self.create_admin(username, password, name)
        else:
            account = self.create_user(username, password, name)
        if account is not None:
                person.add_account(account)
        self.persons.append(person)
        return account
    
    
    def create_user(self, username: str, password: str, name) -> User:
        if self.username_exist(username):
            return None
        user: User = User(username,password, name)
        self.accounts.append(user)
        return self.accounts[-1]
    
    def create_admin(self, username: str, password: str, name: str) -> Admin:
        if self.username_exist(username):
            return None
        admin: Admin = Admin(username,password, name)
        self.accounts.append(admin)
        return self.accounts[-1]
    
    def delete_account(self, account: Account) -> bool:
        try:
            self.accounts.remove(account)
            person = self.check_if_pesron_exist(account.name)
            person.delete_account(account) 
            return True
        except:
            return False
    
    def delete_person(self, person: Person) -> bool:
        try:
            self.persons.remove(person)
            accounts = person.accounts
            for account in accounts:
                self.delete_account(account)
            return True
        except:
            return False
    
    def validate_login(self, username:str, password:str) -> Account:
        for account in self.accounts:
            if account.validate(username, password):
                return account
        return None
        
    
    def change_user_to_admin(self, user: User) -> Admin:
        self.delete_account(user)
        username = user.username
        username: str = user.username
        password: str = user.password
        person_name: str = user.name
        admin: Admin = Admin(username,password,person_name)
        self.accounts.append(admin)
        person: Person = self.check_if_pesron_exist(admin.name)
        person.add_account(admin)
        return self.accounts[-1]
    
    def change_name(self, name: str) -> None:
        self.name = name.title()
        
        
        
    