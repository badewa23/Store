class Item:
    
    def __init__(self, item_name: str, price: float, available: int) -> None:
        self.name = item_name.capitalize()
        self.price = price
        self.qty = available
        
    def get_item_name(self) -> str:
        return self.name
    
    def restock(self, added_qty: int) -> int:
        self.qty += added_qty
        return self.qty
    
    def change_name(self, new_item_name: str) -> str:
        self.name = new_item_name.capitalize()
        return self.name
    
    def get_dictionary_info(self):
            return {"Item_name":self.name, "Price": self.price, "In_stock": self.qty}