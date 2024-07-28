class Stat:
    
    def __init__(self) -> None:
        self.items: dict = dict()
        
    def assign_item_name(self, item_name: str):
        self.item_name = item_name
    
    def assign_unit(self, unit: int):
        self.unit = unit
    
    def assign_person_name(self, name: str):
        self.name = name
    
    def add_unit(self, ammount: int):
        self.unit += ammount
    
    def is_empty(self):
        return len(self.items) == 0
            