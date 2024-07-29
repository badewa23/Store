from Account import Account
from Person import Person
from Item import Item
from Order import Order
from Stat import Stat
from Menu import Menu

class AdminMenu(Menu):
    
    def __init__(self, account: Account, person: Person):
        super().__init__(account.username,account, person)
        self.get_items()
        self.get_persons()
        self.get_accounts()
        self.get_orders()
        self.stat_list: list[Stat] = list()
    
    def display(self):
        while True:
            print(f"{self.name} Admin Menu")
            selection = input("[P]erson Panel\n[A]ccount Panel\n[I]tem Panel\nStore [S]tatistics\n"
                              + "[G]o Back\n[E]xit\n")
            if selection not in "PAISGE" or len(selection) != 1:
                self.CONTROL.clear()
                print("Wrong input please try again\n")
                continue
            match selection:
                case "P":
                    self.CONTROL.clear()
                    status = self.person_panel()
                    if status == 0:
                        self.CONTROL.clear()
                        continue
                    return status
                case "A":
                    self.CONTROL.clear()
                    status = self.account_panel()
                    if status == 0:
                        self.CONTROL.clear()
                        continue
                    return status
                case "I":
                    self.CONTROL.clear()
                    status = self.item_panel()
                    if status == 0:
                        self.CONTROL.clear()
                        continue
                    return status
                case "S":
                    self.CONTROL.clear()
                    self.store_stat_panel()
                    self.CONTROL.clear()
                    continue
                case "G":
                    return 0
                case "E": 
                    return 1
    
    def check_if_stat_exist(self, stat_list: list[Stat], item_name: str) -> Stat | None:
        for stat in stat_list:
            if stat.item_name == item_name:
                return stat
        return None
    
    def store_stat_panel(self) -> None:
        if len(self.stat_list) == 0:
            stat_list: list[Stat] = list()
            for order in self.orders:
                for data in order.dict_items:
                    item_name = data["itemName"]
                    unit = data["unitPurchased"]
                    if len(stat_list) > 0:
                        stat = self.check_if_stat_exist(stat_list, item_name)
                        if stat is not None:
                            stat.add_unit(unit)
                            continue
                    stat = Stat()
                    stat.assign_item_name(item_name)
                    stat.assign_unit(unit)
                    stat_list.append(stat)
            self.stat_list = stat_list
        text = "Item"
        print(f"Store Stat\n{text:<25}Unit Sold")
        for stat in self.stat_list:
            print(f"{stat.item_name:<25}{stat.unit}")
        input(":")  
        return
        
    def check_if_pesron_exist(self, name:str) -> Person | None:
        name = name.title()
        for person in self.persons:
            if person.name == name:
                return person
        return None
    
    def add_person_panel(self):
        self.CONTROL.clear()
        name: str
        age: str
        salary: str
        status = 0
        flag = False
        while True:
            if status == 0:
                name: str = input("Name ([G]o Back): ")
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
                person = self.check_if_pesron_exist(name)
                if person is not None:
                    self.CONTROL.clear()
                    print(f"{name} already exist\n")
                    continue
                status = 1
            if status == 1:
                if flag:
                    print("Name: " + name)
                try:
                    age = input("Age: ")
                    if age == "G":
                        self.CONTROL.clear()
                        return
                    age = int(age)
                    flag = False
                    status = 2
                except:
                    self.CONTROL.clear()
                    print("Please Only Input Digit\n")
                    flag = True
                    continue
            if flag:
                print("Name: " + name)
                print("Age: " + str(age))
            flag: str = input("Does this person have a salary (Y/N): ")
            if flag == "Y":
                try:
                    salary = input("Salary: ")
                    if salary == "G":
                        self.CONTROL.clear()
                        return
                    salary = float(salary)
                    person = Person(name, age, salary)
                    check = self.CONTROL.insert_data_to_persons_collection(person.get_dictionary_info())
                    self.CONTROL.clear()
                    if check:
                        print(f"{person.name} added\n")
                        self.get_persons()
                        return
                    print(f"{person.name} not added\n")
                    return
                except:
                    self.CONTROL.clear()
                    print(f"{salary} need to be a float\n")
                    flag = True
                    continue
            elif flag == "N":
                person = Person(name, age)
                check = self.CONTROL.insert_data_to_persons_collection(person.get_dictionary_info())
                self.CONTROL.clear()
                if check:
                    print(f"{person.name} added\n")
                    self.get_persons()
                    return
                print(f"{person.name} not added\n")
                return
            elif flag == "G":
                self.CONTROL.clear()
                return
            else:
                self.CONTROL.clear()
                print(f"Wrong input please try again\n")
                continue
    
    def person_stat_panel(self, person: Person):
        name = person.name
        stat = Stat()
        stat.assign_person_name(name)
        for order in self.orders:
            if order.name == name:
                dict_items = order.dict_items
                for dict_item in dict_items:
                    item_name = dict_item["itemName"]
                    unit = dict_item["unitPurchased"]
                    items = stat.items
                    if len(items.keys()) > 0:
                        if  item_name in items.keys():
                            items[item_name] += unit
                        else:
                            items[item_name] = unit
                    else:
                        items[item_name] = unit
        if stat.is_empty():
            print(f"{person.name} has not made a purchase")
            input(":")
            self.CONTROL.clear()
            return
        text: str = "Item"
        print(f"{stat.name} Stat\n{text:<25}Purchases")
        for key in stat.items:
            unit = stat.items[key]
            print(f"{key:<25}{unit}")
        input(":")
        self.CONTROL.clear()
        return
    
    def person_panel(self):
        while True:
            num: int =0
            text = "Name"
            text2 = "Age"
            print(f"{text:<23}{text2:<5}Choice")
            for person in self.persons:
                num_text = f"[{num}]"
                print(f"{person.name:<23}{person.age:<5}{num_text:^6}")
                num += 1
            selection = input("[A]dd Person\nPerson [S]tatistics (person)\n[G]o Back\n[E]xit\n")
            if selection in "AGE" and len(selection) == 1:
                match selection:
                    case "A":
                        self.add_person_panel()
                        continue
                    case "G":
                        return 0
                    case "E": 
                        return 1
            elif len(selection.split()) == 2:
                selection = selection.split()
                if selection[0] == "S":
                    num = selection[1]
                    if num.isdigit():
                        num = int(num)
                        if num not in range(len(self.persons)):
                            self.CONTROL.clear()
                            print(f"{num} is not in range\n")
                            continue
                        self.CONTROL.clear()
                        person = self.persons[num]
                        self.person_stat_panel(person)
                    else:
                        self.CONTROL.clear()
                        print(f"{num} is not a digit\n")
                    continue
            self.CONTROL.clear()
            print("Wrong input please try again\n")
            continue
    
    def delete_account(self, account: Account) -> None:
        if account.username == self.account.username:
            print("You can't delete yourself\n")
            return
        result = self.CONTROL.delete_account(account.query_on_username())
        if result > 0:
            print(f"{account.username} deleted\n")
            self.get_accounts()
            return 
        print(f"{account.username} was not deleted\n")
        return
    
    def change_access_pannel(self, account: Account):
        if account.username == self.account.username:
            print("You can't change your own access\n")
            return
        accesses: list[str] = ["Admin","User"]
        while True:
            print(f"{account.username} has {account.access} access")
            text = "Access Type"
            print(f"{text:<15}Choice")
            num: int = 0
            for access in accesses:
                num_text = f"[{num}]"
                print(f"{access:<15}{num_text:^6}")
                num += 1
            choice = input("New Access [G]o Back: ")
            if choice == "G":
                self.CONTROL.clear()
                return
            if choice.isdigit():
                choice = int(choice)
                if choice in range(len(accesses)):
                    new_accesses = accesses[choice]
                    if account.access != new_accesses:
                        check = self.CONTROL.update_data_to_account(account.query_on_username(),
                                                            account.new_access_update(new_accesses))
                        if check:
                            self.CONTROL.clear()
                            self.get_accounts()
                            print(f"{account.username} is now an {new_accesses}\n")
                            return
                        else:
                            self.CONTROL.clear()
                            print(f"{account.username} could not become a {new_accesses}\n")
                            continue
                    else:
                        self.CONTROL.clear()
                        if new_accesses == "Admin":
                            print(f"{account.username} is already an {new_accesses}\n")
                        else:
                            print(f"{account.username} is already a {new_accesses}\n")
                        continue
                else:
                    self.CONTROL.clear()
                    print(f"{choice} is not in range\n")
                    continue
            else:
                self.CONTROL.clear()
                print(f"{choice} is not a digit\n")
                continue
    
    def account_panel(self):
        while True:
            num: int =0
            text = "Username"
            text2 = "Person"
            text3 = "Access Type"
            print(f"{text:<12}{text2:<21}{text3:<15}Choice")
            for account in self.accounts:
                num_text = f"[{num}]"
                print(f"{account.username:<12}{account.name:<21}{account.access:<15}{num_text:^6}")
                num += 1
            selection = input("[D]elete (account)\n[C]hange access\n[G]o Back\n[E]xit\n")
            if selection in "GE" and len(selection) == 1:
                match selection:
                    case "G":
                        return 0
                    case "E": 
                        return 1
            elif len(selection.split()) == 2:
                selection = selection.split()
                match selection[0]:
                    case "D":
                        num:str = selection[1]
                        if num.isdigit():
                            num = int(num)
                            if num not in range(len(self.accounts)):
                                self.CONTROL.clear()
                                print(f"{num} is not in range\n")
                                continue
                            self.CONTROL.clear()
                            account = self.accounts[num]
                            self.delete_account(account)
                        else:
                            self.CONTROL.clear()
                            print(f"{num} is not a digit\n")
                        continue
                    case "C":
                        num:str = selection[1]
                        if num.isdigit():
                            num = int(num)
                            if num not in range(len(self.accounts)):
                                self.CONTROL.clear()
                                print(f"{num} is not in range\n")
                                continue
                            self.CONTROL.clear()
                            account = self.accounts[num]
                            self.change_access_pannel(account)
                        else:
                            self.CONTROL.clear()
                            print(f"{num} is not a digit\n")
                        continue
            self.CONTROL.clear()
            print("Wrong input please try again\n")
            continue
    
    def delete_item(self, item: Item) -> None:
        result = self.CONTROL.delete_item(item.query_on_item_name())
        if result > 0:
            print(f"{item.name} deleted\n")
            self.get_items()
            return 
        print(f"{item.name} was not deleted\n")
        return
    
    def check_if_item_exist(self, name:str) -> Item | None:
        name = name.capitalize()
        for item in self.items:
            if item.name == name:
                return item
        return None
    
    def add_item_panel(self):
        name: str
        description: str
        price: float
        unit: int
        plural: str
        age_restriction: str
        status = 0
        flag = False
        while True:
            if status == 0:
                name: str = input("Item name ([G]o Back): ")
                if name == "G":
                    self.CONTROL.clear()
                    return
                if name.isdigit():
                    self.CONTROL.clear()
                    print(f"{name} can't be numbers only\n")
                    continue
                item = self.check_if_item_exist(name)
                if item is not None:
                    self.CONTROL.clear()
                    print(f"{name} already exist\n")
                    continue
                status = 1
            if status == 1:
                if flag:
                    print("Item Name: " + name)
                description: str = input("Item description: ")
                if description == "G":
                    self.CONTROL.clear()
                    return
                if description.isdigit():
                    self.CONTROL.clear()
                    print(f"{description} can't be numbers only\n")
                    flag = True
                    continue
                flag = False
                status = 2
            if status == 2:
                if flag:
                    print("Item Name: " + name)
                    print("Description: " + description)
                try:
                    price = input("Item price: ")
                    if price == "G":
                        self.CONTROL.clear()
                        return
                    price = float(price)
                    flag = False
                    status = 3
                except:
                    self.CONTROL.clear()
                    print(f"{price} need to be a float\n")
                    flag = True
                    continue
            if status == 3:
                if flag:
                    print("Item Name: " + name)
                    print("Description: " + description)
                    print("Price: " + str(price))
                try:
                    unit = input("Quantity: ")
                    if unit == "G":
                        self.CONTROL.clear()
                        return
                    unit = int(unit)
                    flag = False
                    status = 4
                except:
                    self.CONTROL.clear()
                    print(f"{unit} need to be a digit\n")
                    flag = True
                    continue
            if status == 4:
                if flag:
                    print("Item Name: " + name)
                    print("Description: " + description)
                    print("Price: " + str(price))
                    print("Unit: " + str(unit))
                plural = input("Plural of the item name: ")
                if plural == "G":
                    self.CONTROL.clear()
                    return
                if plural.isdigit():
                    self.CONTROL.clear()
                    print(f"{plural} can't be numbers only\n")
                    flag = True
                    continue
                flag = False
                status = 5
            if flag:
                print("Item Name: " + name)
                print("Description: " + description)
                print("Price: " + str(price))
                print("Unit: " + str(unit))
                print("Plural: " + plural)
            check: str = input("Does this item have age restrictions (Y/N): ")
            if check == "Y":
                try:
                    age_restriction = input("Age restrictions: ")
                    if age_restriction == "G":
                        self.CONTROL.clear()
                        return
                    age_restriction = int(age_restriction)
                    item = Item(name,price,unit,description,plural,age_restriction)
                    check = self.CONTROL.insert_data_to_items_collection(item.get_dictionary_info())
                    self.CONTROL.clear()
                    if check:
                        print(f"{item.name} added")
                        self.get_items()
                        return
                    print(f"{item.name} not added")
                    return
                except:
                    self.CONTROL.clear()
                    print(f"{age_restriction} need to be a digit\n")
                    flag = True
                    continue
            elif check == "N":
                item = Item(name,price,unit,description,plural)
                check = self.CONTROL.insert_data_to_items_collection(item.get_dictionary_info())
                self.CONTROL.clear()
                if check:
                    print(f"{item.name} added")
                    self.get_items()
                    return
                print(f"{item.name} not added")
                return
            elif check == "G":
                self.CONTROL.clear()
                return
            else:
                self.CONTROL.clear()
                print(f"Wrong input please try again\n")
                continue
            
    def restock(self, item: Item, ammount: int):
        self.CONTROL.clear()
        if self.CONTROL.update_data_to_item(item.query_on_item_name(),item.restock(ammount)):
            print(f"{item.name} restocked\n")
            self.get_items()
            return 
        print(f"{item.name} was not restocked\n")
        self.get_items()
        return
        
    def item_panel(self):
        while True:
            num: int =0
            text = "Item Name"
            text2 = "Price"
            text3 = "Unit"
            text4 = "Age Restrictions"
            number = 7
            print(f"{text:<24}{text2:<7}{text3:<7}{text4:<18}Choice")
            for item in self.items:
                num_text = f"[{num}]"
                text = "None"
                if item.ageRestrictions == -1:
                    print(f"{item.name:<24}${item.price:<6.2f}{item.qty:<7}{text:<18}{num_text:^6}")
                else:
                    print(f"{item.name:<24}${item.price:<6.2f}{item.qty:<7}{item.ageRestrictions:<18}{num_text:^6}")
                num += 1
            selection = input("[D]elete (item)\n[A]dd (item)\n[R]estock (item ammount)\n[G]o Back\n[E]xit\n")
            if selection in "AGE" and len(selection) == 1:
                match selection:
                    case "A":
                        self.CONTROL.clear()
                        self.add_item_panel()
                        continue
                    case "G":
                        return 0
                    case "E": 
                        return 1
            elif len(selection.split()) == 2:
                selection = selection.split()
                match selection[0]:
                    case "D":
                        num = selection[1]
                        if num.isdigit():
                            num = int(num)
                            if num not in range(len(self.items)):
                                self.CONTROL.clear()
                                print(f"{num} is not in range\n")
                                continue
                            self.CONTROL.clear()
                            item = self.items[num]
                            self.delete_item(item)
                        else:
                            self.CONTROL.clear()
                            print(f"{num} is not a digit\n")
                        continue
            elif len(selection.split()) == 3:
                selection = selection.split()
                if selection[0] == "R":
                    num = selection[1]
                    ammount = selection[2]
                    if num.isdigit():
                        num = int(num)
                        if num in range(len(self.items)):
                            item = self.items[num]
                        else:
                            self.CONTROL.clear()
                            print(f"{num} is not in range\n")
                            continue
                        if ammount.isdigit():
                            ammount = int(ammount)
                            self.restock(item,ammount)
                        else:
                            self.CONTROL.clear()
                            print(f"{ammount} is not an whole number\n")
                    else:
                        self.CONTROL.clear()
                        print(f"{num} is not a digit\n")
                    continue
            self.CONTROL.clear()
            print("Wrong input please try again\n")
            continue