from Account import Account
from Person import Person
from Item import Item
from CheckoutItem import CheckoutItem
from Order import Order
from Menu import Menu

class UserMenu(Menu):
    
    def __init__(self, account: Account, person: Person):
        super().__init__(account.username,account, person)
        self.get_items()
        self.checkout_items: list[CheckoutItem] = list()
    
    def display(self) -> int:
        while True:
            print(f"{self.name} User Menu")
            selection = input("[C]heckout Panel\n[B]rowse\n[G]o Back\n[E]xit\n")
            if selection not in "CBGE" or len(selection) != 1:
                self.CONTROL.clear()
                print("Wrong input please try again\n")
            match selection:
                case "C":
                    self.CONTROL.clear()
                    status = self.checkout_panel()
                    if status == 0:
                        self.CONTROL.clear()
                        continue
                    elif status == 2:
                        continue
                    return status
                case "B":
                    self.CONTROL.clear()
                    status = self.browse_item_panel()
                    if status == 0:
                        self.CONTROL.clear()
                        continue
                    elif status == 2:
                        continue
                    return status
                case "G":
                    if self.account.access == "Admin":
                        return 2
                    return 0
                case "E": 
                    return 1
    
    def checkout_panel(self) -> int:
        if len(self.checkout_items) == 0:
            print("You have not checkout an item\n")
            return 2
        while True:
            count: int = 0
            total: int = 0
            text = "Item Name"
            text2 = "Price"
            text3 = "Unit"
            text4 = "Total"
            print(f"{text:<24}{text2:<7}{text3:<7}{text4:<10}Choice")
            for checkout_item in self.checkout_items:
                num_text = f"[{count}]"
                line = checkout_item.__str__() + f"{num_text:^6}"
                print(line)
                total += checkout_item.get_total()
                count += 1
            text = f"${total:.2f}"
            print(f"Total{text:>40}")
            selection = input("[C]heckout\n[R]emove (item opt:ammount)\n[G]o Back\n[E]xit\n")
            if selection in "CGE" and len(selection) == 1:
                match selection:
                    case "C":
                        self.CONTROL.clear()
                        for checkout_item in self.checkout_items:
                            item: Item = self.check_if_item_exist(checkout_item.name)
                            self.CONTROL.update_data_to_item(checkout_item.query_on_item(), 
                                                                item.new_qty_update(checkout_item.unit))
                        self.create_order()
                        self.CONTROL.insert_data_to_orders_collection(self.order.get_dictionary_info())
                        self.checkout_items = list()
                        self.get_items()
                        print("Checkout Complete\n")
                        return 2                  
                    case "G":
                        return 0
                    case "E": 
                        return 1
            elif(len(selection.split()) == 2):
                selection = selection.split()
                if selection[0] == "R":
                    num = selection[1]
                    if num.isdigit():
                        num = int(num)
                        if num in range(len(self.checkout_items)):
                            checkout_item: CheckoutItem =self.checkout_items.pop(num)
                            self.CONTROL.clear()
                            print(f"{checkout_item.plural} removed from Checkout\n")
                        else:
                            self.CONTROL.clear()
                            print(f"{num} is not in range\n")
                    else:
                        self.CONTROL.clear()
                        print(f"{num} is not a digit\n")
                    continue
            elif(len(selection.split()) == 3):
                selection = selection.split()
                if selection[0] == "R":
                    num = selection[1]
                    ammount = selection[2]
                    if num.isdigit():
                        num = int(num)
                        if num in range(len(self.checkout_items)):
                            checkout_item = self.checkout_items[num]
                        else:
                            self.CONTROL.clear()
                            print(f"{num} is not in range\n")
                            continue
                        if ammount.isdigit():
                            ammount = int(ammount)
                            if checkout_item.remove_ammount(ammount):
                                self.CONTROL.clear()
                                print(f"{ammount} {checkout_item.plural} removed from Checkout\n")
                                continue
                            else:
                                self.CONTROL.clear()
                                print("You remove more than is available\n")
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
    
    def browse_item_panel(self) -> int:
        while True:
            count: int = 0
            text = "Item Name"
            text2 = "Description"
            text3 = "Price"
            print(f"{text:<24}{text2:<35}{text3:<7}Choice")
            for item in self.items:
                num_text = f"[{count}]"
                line = item.__str__() + f"{num_text:^6}"
                print(line)
                count += 1
            selection = input("[B]uy (item ammount)\n[G]o Back\n[E]xit\n")
            if selection in "GE" and len(selection) == 1:
                match selection:
                    case "G":
                        return 0
                    case "E": 
                        return 1
            elif(len(selection.split()) == 3):
                selection = selection.split()
                if selection[0] == "B":
                    num = selection[1]
                    ammount = selection[2]
                    if num.isdigit():
                        num = int(num)
                        if num in range(len(self.items)):
                            item: Item =self.items[num]
                        else:
                            self.CONTROL.clear()
                            print(f"{num} is not in range\n")
                            continue
                        if ammount.isdigit():
                            ammount = int(ammount)
                            if len(self.checkout_items) > 0:
                                checkout_item = self.check_if_checkout_item_exist(item.name)
                                if checkout_item is not None:
                                    sum = ammount + checkout_item.unit
                                    if item.check_if_ammount_is_available(sum):
                                        checkout_item.add_ammount(ammount)
                                        self.CONTROL.clear()
                                        print(f"{ammount} {item.plural} have been added to Checkout\n")
                                        continue
                                    else:
                                        self.CONTROL.clear()
                                        print(f"{ammount} more {checkout_item.plural} is not available\n")
                                else:
                                    if item.check_if_ammount_is_available(ammount):
                                        checkout_item = item.create_checkout_item(ammount)
                                        self.checkout_items.append(checkout_item)
                                        self.CONTROL.clear()
                                        print(f"{ammount} {item.plural} have been added to Checkout\n")
                                        continue
                                    else:
                                        self.CONTROL.clear()
                                        print(f"{ammount} {item.plural} is not available\n")
                            else:
                                if item.check_if_ammount_is_available(ammount):
                                            checkout_item = item.create_checkout_item(ammount)
                                            self.checkout_items.append(checkout_item)
                                            self.CONTROL.clear()
                                            print(f"{ammount} {item.plural} have been added to Checkout\n")
                                            continue
                                else:
                                    self.CONTROL.clear()
                                    print(f"{ammount}  {item.plural} is not available\n")
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
    
    def create_order(self):
        self.order: Order = Order(self.person.name)
        self.order.add_checkout_item_list(self.checkout_items)
    
    def check_if_checkout_item_exist(self, item_name):
        for checkout_item in self.checkout_items:
            if checkout_item.name == item_name:
                return checkout_item
        return None
    
    def check_if_item_exist(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None
            