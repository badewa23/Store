class CheckoutItem:
    
    def __init__(self, name:str, price: float, unit: int, plural: str) -> None:
        self.name = name.title()
        self.unit = unit
        self.price = price
        self.plural = plural.title()
    
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
        total = self.get_total()
        return f"{self.name:<24}${self.price:<6.2f}{self.unit:<7}${total:<10.2f}"