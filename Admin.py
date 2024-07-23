from Account import Account as A

class Admin(A):
    
    def __init__(self, username: str, password: str, name:str):
        super().__init__(username, password, "Admin", name)
        