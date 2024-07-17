class Item:
    
    def __init__(self, item_name: str, available: int) -> None:
        self.name = item_name.capitalize()
        self.qty = available
    
    def restock(self, added_qty: int) -> int:
        self.qty += added_qty
        return self.qty
    
    def change_name(self, new_item_name: str) -> str:
        self.name = new_item_name.capitalize()
        return self.name