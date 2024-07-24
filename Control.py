from pymongo import MongoClient
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
        
        if "persons" in collection_ist:
            self.LOG.add_logging_info("Getting Persons Collection into Store Database")
            self.person = self.database.persons
        else:
            self.LOG.add_logging_info("Create Persons Collection into Store Database")
            self.person = self.database["persons"]
        
        if "items" in collection_ist:
            self.LOG.add_logging_info("Getting Items Collection into Store Database")
            self.person = self.database.items
        else:
            self.LOG.add_logging_info("Create Items Collection into Store Database")
            self.person = self.database["items"]
        
        if "accounts" in collection_ist:
            self.LOG.add_logging_info("Getting Accounts Collection into Store Database")
            self.person = self.database.accounts
        else:
            self.LOG.add_logging_info("Create Accounts Collection into Store Database")
            self.person = self.database["accounts"]
    
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
    
    def update_data_to_account(self, query: dict, set: dict):
        self.LOG.add_logging_info("Updating an Account")
        try:
            self.database.accounts.update_one(query, set)
        except:
            self.LOG.add_logging_error("Fail to update Account")
    