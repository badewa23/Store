from Account import Account
from Person import Person
from Item import Item
from Order import Order
from Menu import Menu

class AdminMenu(Menu):
    
    def __init__(self, account: Account, person: Person):
        super().__init__(account.username,account, person)
        self.get_items()
        self.get_persons()
        self.get_accounts()
        self.get_orders()
    
    def dislpay(self):
        while True:
            print(f"{self.name} Admin Menu")
            selection = input("[P]erson Panel\n[A]ccount Panel\n[I]tem Panel\nStore [S]tatistics\n"
                              + "[G]o Back\n[E]xit\n")
            if selection not in "PAISGE" or len(selection) != 1:
                self.CONTROL.clear()
                print("Wrong input please try again\n")
            match selection:
                case "G":
                    return 0
                case "E": 
                    return 1