from CheckoutItem import CheckoutItem 
class Order:
    
    def __init__(self, name) -> None:
        self.name = name
    
    def add_item(self, checkout_item):
        self.checkout_items.append(checkout_item)
    
    def add_checkout_item_list(self, checkout_items: list[CheckoutItem] ):
        self.checkout_items: list[CheckoutItem] = checkout_items
    
    def add_dict_list(self, ditc_list: list[dict]):
        self.dict_items = ditc_list
    
    def get_dictionary_info(self):
        items: list[dict] = list()
        for item in self.checkout_items:
            dictionary = {"itemName":item.name, "unitPurchased": item.unit}
            items.append(dictionary)
        return {"name":self.name, "items":items}