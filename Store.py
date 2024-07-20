from User import User
from Admin import Admin
from Account import Account
from Item import Item

class Store:

    def __init__(self, name: str):
        self.name: str = name.title()
        self.inventory: list = list()
        self.accounts: list = list()
    
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
    
    def create_user(self, username: str, password: str, name: str, age: int) -> User:
        if self.username_exist(username):
            return None
        user: User = User(username,password,name,age)
        self.accounts.append(user)
        return self.accounts[-1]
    
    def delete_user(self, user: User) -> bool:
        try:
            self.accounts.remove(user)
            return True
        except:
            return False
    
    def create_admin(self, username: str, password: str, name: str, age: int) -> Admin:
        if self.username_exist(username):
            return None
        admin: Admin = Admin(username,password,name,age)
        self.accounts.append(admin)
        return self.accounts[-1]
    
    def delete_admin(self, admin: Admin) -> bool:
        try:
            self.accounts.remove(admin)
            return True
        except:
            return False
    
    def validate_login(self, username:str, password:str) -> Account:
        for account in self.accounts:
            if account.validate(username, password):
                return account
        return None

    
    def change_user_to_admin(self, username: str) -> Admin:
        index: int
        for num in range(len(self.accounts)):
            account = self.accounts[num]
            if username == account.get_username():
                index = num
        user: User = self.accounts[index]
        info: tuple = user.get_info()
        username: str = info[0]
        password: str = info[1]
        name: str = info[2]
        age: int = info[3]
        admin: Admin = Admin(username,password,name,age)
        self.accounts[index] = admin
        return self.accounts[index]
    
    def change_name(self, name: str) -> None:
        self.name = name.title()
        
        
    