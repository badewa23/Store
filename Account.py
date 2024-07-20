class Account():
    
    def __init__(self, username: str, password: str, name: str, age: int) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.name = name.title()
        self.age = age
    
    def get_username(self) -> str:
        return self.username
    
    def validate(self, username: str, password: str) -> bool:
        return username == self.username and password == self.password
    
    def display(self):
        pass