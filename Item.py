from CheckoutItem import CheckoutItem

class Item:
    
    def __init__(self, item_name: str, price: float, available: int, description: str, plural:str, 
                 ageRestrictions: int = None):
        self.name = item_name.title()
        self.plural = plural
        self.price = price
        self.description = description.capitalize()
        self.ageRestrictions = ageRestrictions
        self.qty = available
        
    def create_checkout_item(self, unit):
        checkoutItem: CheckoutItem = CheckoutItem(self.name,self.price,unit,self.plural)
        return checkoutItem
        
    def get_item_name(self) -> str:
        return self.name
    
    def check_if_ammount_is_available(self, ammount: int):
        new_qty = self.qty - ammount
        return new_qty >= 0
    
    def new_qty_update(self, ammount: int) -> dict:
        new_qty = self.qty - ammount
        return {"$set": {"inStock": new_qty}}
    
    def restock(self, added_qty: int) -> int:
        new_qty = self.qty + added_qty
        return  {"$set": {"inStock": new_qty}}
    
    def change_name(self, new_item_name: str) -> str:
        self.name = new_item_name.capitalize()
        return self.name
    
    def get_dictionary_info(self):
        if  self.ageRestrictions is None:
            return {"itemName":self.name,"description":self.description, "price": self.price,
                    "inStock": self.qty, "plural": self.plural}
        return {"itemName":self.name,"description":self.description, "price": self.price,
                    "inStock": self.qty, "plural": self.plural, "ageRestrictions":self.ageRestrictions}
    
    def query_on_item_name(self) -> dict:
        return {"itemName":self.name}
    
    def __str__(self) -> str:
        return f"{self.name}    {self.description}  $%.2f" %self.price