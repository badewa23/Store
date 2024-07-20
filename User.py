from Account import Account as A

class User(A):
    def __init__(self, username: str, password: str, name: str, age: int):
        super().__init__(username, password, name, age)
        
    def get_info(self) -> tuple:
        return self.username, self.password, self.name, self.age
    