from Control import Control
from Item import Item
from Account import Account
from Person import Person
from Order import Order

class Menu:
    CONTROL: Control = Control()
    
    def __init__(self, name: str = None, account: Account = None, person: Person = None):
        self.name = name
        self.account = account
        self.person = person
    
    def get_orders(self):
        orders = self.CONTROL.get_orders()
        self.orders: list[Order] = list()
        for order in orders:
            a_order = self.create_order(order)
            self.orders.append(a_order)
    
    def create_order(self, orders: dict) -> Order:
        name = orders["name"]
        items = orders["items"]
        order: Order = Order(name)
        order.add_dict_list(items)
        return order
    
    def get_persons(self):
        persons = self.CONTROL.get_persons()
        self.persons: list[Person] = list()
        for person in persons:
            a_person = self.create_person(person)
            self.persons.append(a_person)
    
    def create_person(self, person: dict) -> Person:
        name = person["name"]
        age = person["age"]
        if "salary" in person.keys():
            salary = person["salary"]
            return Person(name, age, salary)
        return Person(name,age)
    
    def get_accounts(self):
        accounts = self.CONTROL.get_accounts()
        self.accounts: list[Account] = list()
        for account in accounts:
            user = self.create_account(account)
            self.accounts.append(user)
    
    def create_account(self,account: dict) -> Account:
        username = account["username"]
        password = account["password"]
        person_name = account["name"]
        access = account["access"]
        return Account(username,password,access,person_name)
    
    def get_items(self):
        items = self.CONTROL.get_items()
        self.items: list[Item] = list()
        for item in items:
            item_1 = self.create_item(item)
            if item_1 is not None:
                self.items.append(item_1)
    
    def create_item(self, item: dict) -> Person:
        name = item["itemName"]
        description = item["description"]
        price = float(item["price"])
        plural = item["plural"]
        inStock = item["inStock"]
        if inStock >0:
            if "ageRestrictions" in item.keys():
                ageRestrictions = item["ageRestrictions"]
                if self.person.age >= ageRestrictions: 
                    return Item(name, price, inStock, description, plural, ageRestrictions)
                return None
            return Item(name, price, inStock, description, plural)
        return None