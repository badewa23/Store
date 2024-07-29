from Menu import Menu 
from UserMenu import UserMenu
from AdminMenu import AdminMenu
from Account import Account
from Person import Person

class AccountMenu(Menu):
    
    def __init__(self, account: Account, person: Person ):
        super().__init__(None,account,person)
    
    def display(self) -> int:
        choice: str = self.account.display(self.CONTROL.clear)
        self.CONTROL.clear()
        while True:
            match choice:
                case "U":
                    user_menu = UserMenu(self.account,self.person)
                    status = user_menu.display()
                    if status == 2:
                        self.CONTROL.clear()
                        choice: str = self.account.display(self.CONTROL.clear)
                        continue
                    return status
                case "G":
                    return 0
                case "A":
                    self.CONTROL.clear()
                    admin_menu = AdminMenu(self.account,self.person)
                    status = admin_menu.display()
                    if status == 0:
                        self.CONTROL.clear()
                        choice: str = self.account.display(self.CONTROL.clear)
                        self.CONTROL.clear()
                        continue
                    return status
                case "E": 
                    return 1