from Account import Account as A

class Admin(A):
    
    def __init__(self, username: str, password: str, name: str, age: int):
        super().__init__(username, password, name, age)
        