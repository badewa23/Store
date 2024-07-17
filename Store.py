from User import User
from Admin import Admin
from Account import Account

class Store:

    def __init__(self, name: str):
        self.name: str = name
        self.items: list = list()
        self.accounts: list = list()
        self.number_of_accounts: int = 0
        self.username_and_password_dict: dict = dict()
        
    def create_user(self, username: str, password: str, name: str, age: int) -> User:
        user: User = User(username,password,name,age)
        self.accounts.append(user)
        user: User = self.accounts[-1]
        username: str = user.username
        password: str = user.password
        self.username_and_password_dict[username] = [password, self.number_of_accounts]
        self.number_of_accounts +=1
        return user
    
    def create_admin(self, username: str, password: str, name: str, age: int) -> Admin:
        admin: Admin = Admin(username,password,name,age)
        self.accounts.append(admin)
        admin: Admin = self.accounts[-1]
        username: str = admin.username
        password: str = admin.password
        self.username_and_password_dict[username] = [password, self.number_of_accounts]
        self.number_of_accounts +=1
        return admin
    
    def validate_login(self, username, password) -> Account:
        keys = self.username_and_password_dict.keys()
        if  username in keys:
            listed: list = self.username_and_password_dict[username]
            if password == listed[0]:
                num = listed[1]
                return self.accounts[num]
        return None
                

    def change_user_to_admin(self, user: User) -> Admin:
        username: str = user.username
        postion = self.username_and_password_dict[username][1]
        user: User = self.accounts[postion]
        info: tuple = user.get_info()
        username: str = info[0]
        password: str = info[1]
        name: str = info[2]
        age: int = info[3]
        admin: Admin = Admin(username,password,name,age)
        self.accounts[postion] = admin
        return self.accounts[postion]
        
        
    