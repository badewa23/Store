from Account import Account as A

class User(A):
    def __init__(self, username: str, password: str, name:str):
        super().__init__(username, password, "User", name)
    