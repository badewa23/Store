from pymongo import MongoClient
from os import system, name
import json
from Log import Log
class Control:
    LOG:Log = Log()
    LOG.add_logging_info("Connection to MongoDB Local")
    
    try:
        CLIENT = MongoClient()
    except:
        LOG.add_logging_error("Failed to Connect to MongoDB local")
    
    def __init__(self, datbase = "store"):
        self.LOG.add_logging_info("List of Database in MongoDB")
        database_list: list[str] = self.CLIENT.list_database_names()
        
        if datbase in database_list:
            self.LOG.add_logging_info("Going to Store Database in MongoDB")
            self.database = self.CLIENT.get_database(datbase)
        else:
            self.LOG.add_logging_info("Create Store Database into MongoDB")
            self.database = self.CLIENT[datbase]
            
        self.LOG.add_logging_info("List of Collection in Store Database")
        collection_ist = self.database.list_collection_names()
        
        if "persons" not in collection_ist:
            self.LOG.add_logging_info("Getting persons.json into Persons Collection")
            self.add_persons_json()
        
        if "items" not in collection_ist:
            self.LOG.add_logging_info("Getting items.json into Items Collection")
            self.add_items_json()
        
        if "accounts" not in collection_ist:
            self.LOG.add_logging_info("Getting accounts.json into Accounts Collection")
            self.add_accounts_json()
    
    def add_persons_json(self):
        with open('persons.json') as f:
            persons_data = json.load(f)
        self.database.persons.insert_many(persons_data)
    
    def add_items_json(self):
        with open('items.json') as f:
            items_data = json.load(f)
        self.database.items.insert_many(items_data)
        
    def add_accounts_json(self):
        with open('accounts.json') as f:
            accounts_data = json.load(f)
        self.database.accounts.insert_many(accounts_data)
        
    def insert_data_to_persons_collection(self, person_info: dict):
        self.LOG.add_logging_info("Add a Person Collection into Persons Collection")
        try:
            self.database.persons.insert_one(person_info)
        except:
            self.LOG.add_logging_error("Fail to add Person to Persons Collection")
    
    def insert_data_to_items_collection(self, item_info: dict):
        self.LOG.add_logging_info("Add an Item into Items Collection")
        try:
            self.database.items.insert_one(item_info)
        except:
            self.LOG.add_logging_error("Fail to add Item to Items Collection")
    
    def insert_data_to_accounts_collection(self, account_info: dict):
        self.LOG.add_logging_info("Add an Account  into Accounts Collection")
        try:
            self.database.accounts.insert_one(account_info)
        except:
            self.LOG.add_logging_error("Fail to add Account to Accounts Collection")
    
    def insert_data_to_orders_collection(self, order_info: dict):
        self.LOG.add_logging_info("Add an Order into Order Collection")
        try:
            self.database.orders.insert_one(order_info)
        except:
            self.LOG.add_logging_error("Fail to add Order to Order Collection")
    
    def update_data_to_account(self, query: dict, set: dict):
        self.LOG.add_logging_info("Updating an Account Document")
        try:
            self.database.accounts.update_one(query, set)
        except:
            self.LOG.add_logging_error("Fail to update Account Document")
    
    def update_data_to_item(self, query: dict, set: dict):
        self.LOG.add_logging_info("Updating an Item Document")
        try:
            self.database.items.update_one(query, set)
        except:
            self.LOG.add_logging_error("Fail to update Item Document")
    
    def get_accounts(self):
        self.LOG.add_logging_info("Getting Accounts Collection's Documents")
        try:
            return self.database.accounts.find({},{"username":1,"password":1,"name":1,"access":1,"_id":0})
        except:
            self.LOG.add_logging_error("Fail to get Accounts Collection's Documents")
    
    def get_persons(self):
        self.LOG.add_logging_info("Getting Persons Collection's Documents")
        try:
            return self.database.persons.find({},{"name":1,"age":1,"salary":1,"_id":0})
        except:
            self.LOG.add_logging_error("Fail to get Persons Collection's Documents")
    
    def get_items(self):
        self.LOG.add_logging_info("Getting Items Collection's Documents")
        try:
            return self.database.items.find({},{"itemName":1,"description":1,"price":1,"inStock":1,
                                                  "ageRestrictions":1,"plural":1,"_id":0})
        except:
            self.LOG.add_logging_error("Fail to get Items Collection's Documents")
    
    def get_orders(self):
        self.LOG.add_logging_info("Getting Orders Collection's Documents")
        try:
            return self.database.orders.find({},{"name":1,"items":1,"_id":0})
        except:
            self.LOG.add_logging_error("Fail to get Orders Collection's Documents")
    
    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    