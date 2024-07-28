from Menu import Menu 
from AccountMenu import AccountMenu
from Account import Account
from Person import Person

class StoreMenu(Menu):
    def __init__(self, name: str = "General"):
        super().__init__(name)
        self.accesses: list =["User","Admin"]
        self.get_accounts()
        self.get_persons()
    
    def display(self) -> None:
        while True:
            print(f"Welcome To {self.name} store")
            selection: str = input("[L]ogin\n[C]reate Account\n[E]xit\n")
            if selection not in "LCE" or len(selection) != 1:
                self.CONTROL.clear()
                print("Wrong input please try again\n")
                continue
            match selection:
                case "L":
                    print()    
                    username: str = input("Username: ")
                    passowrd: str = input("Password: ")
                    account = self.validate_login(username,passowrd)
                    if account is None:
                        self.CONTROL.clear()
                        print("Wrong Username or Password\n")
                        continue
                    person = self.check_if_pesron_exist(account.name)
                    self.CONTROL.clear()
                    account_menu = AccountMenu(account,person)
                    status = account_menu.display()
                    if status == 1:
                        self.CONTROL.clear()
                        return
                    self.CONTROL.clear()
                    continue
                case "C":
                    self.CONTROL.clear()
                    info: tuple = self.create_account_panel()
                    if info == 0:
                        print("Back to Store Menu")
                        continue
                    elif info == 1:
                        continue
                    account: Account = info[0]
                    person: Person = info[1]
                    control: int = info[2]
                    account_menu: AccountMenu = AccountMenu(account,person)
                    if control == 1:
                        self.CONTROL.insert_data_to_accounts_collection(account.get_dictionary_info())
                        self.CONTROL.insert_data_to_persons_collection(person.get_dictionary_info())
                    else:
                        self.CONTROL.insert_data_to_accounts_collection(account.get_dictionary_info())
                    self.CONTROL.clear()
                    status = account_menu.display()
                    if status == 1:
                        self.CONTROL.clear()
                        return
                    self.reload()
                    self.CONTROL.clear()
                    continue
                case "E":
                    self.CONTROL.clear()
                    return
    
    def reload(self) -> None:
        self.__init__()
    
    def create_account_panel(self) -> object:
        while True:
            print("Creating Account ([G]o Back):") 
            while True:   
                username: str = input("Username: ")
                if username == "G":
                    self.CONTROL.clear()
                    return 0
                if self.username_exist(username):
                    self.CONTROL.clear()
                    print("Duplicate Username\n")
                    continue
                else:
                    break
            passowrd: str = input("Password: ")
            if passowrd == "G":
                    self.CONTROL.clear()
                    return 0
            while True:
                name: str = input("Name: ")
                if name == "G":
                    self.CONTROL.clear()
                    return
                if any(i.isdigit() for i in name):
                    self.CONTROL.clear()
                    print("Please Only Input in Alphabet\n")
                    continue
                else:
                    if len(name.split()) > 2 or len(name.split()) < 2:
                        self.CONTROL.clear()
                        print("Please Only Input A First Name And Last Name\n")
                        continue
                break
            person = self.check_if_pesron_exist(name)
            if person is not None:
                if self.account_have_name(name):
                    self.CONTROL.clear()
                    print("Person Already Has An Account")
                    return 1
                self.CONTROL.clear()
                return (Account(username, passowrd, self.accesses[0], person.name), person, 0)
            age: str = input("Age: ")
            if age == "G":
                self.CONTROL.clear()
                return 0
            if age.isdigit():
                age: int = int(age)
            else:
                self.CONTROL.clear()
                print("Please Only Input Digit\n")
                continue
            return (Account(username, passowrd, self.accesses[0], name), Person(name,age), 1)
            
    def validate_login(self, username:str, password:str) -> Account | None:
        for account in self.accounts:
            if account.validate(username, password):
                return account
        return None
    
    def username_exist(self, username: str) -> bool:
        for account in self.accounts:
            if account.username == username:
                return True
        return False
    
    def account_have_name(self,name: str) -> bool:
        name = name.title()
        for account in self.accounts:
            if account.name == name:
                return True
        return False
    
    def check_if_pesron_exist(self, name:str) -> Person | None:
        name = name.title()
        for person in self.persons:
            if person.name == name:
                return person
        return None