class CheckoutItem:
    
    def __init__(self, name:str, price: float, unit: int, plural: str) -> None:
        self.name = name.capitalize()
        self.unit = unit
        self.price = price
        self.plural = plural
    
    def get_total(self) -> float:
        return self.unit*self.price
    
    def query_on_item(self) -> dict:
        return {"itemName": self.name}
    
    def add_ammount(self, ammount):
        self.unit += ammount
        
    def remove_ammount(self, ammount) -> bool:
        new_unit = self.unit - ammount
        if new_unit < 0:
            return False
        self.unit = new_unit
        return True
    
    def __str__(self) -> str:
        total = self.price * self.unit
        return f"{self.name}    $%.2f   {self.unit}    $%.2f"%(self.price, total)