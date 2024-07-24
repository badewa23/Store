from abc import ABC, abstractmethod
class Account(ABC):
    
    def __init__(self, username: str, password: str, access: str, name: str) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.name = name
        self.access = access
    
    def get_username(self) -> str:
        return self.username
    
    def validate(self, username: str, password: str) -> bool:
        return username == self.username and password == self.password
    
    @abstractmethod
    def display(self):
        pass
    
    def get_dictionary_info(self):
            return {"Username":self.username, "Password": self.password, 
                    "Person_name": self.name, "Access": self.access}
    def query_on_username(self):
        return {"Username":self.username}