class Account():
    
    def __init__(self, username: str, password: str, access: str, name: str) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.name = name.title()
        self.access = access
    
    def get_username(self) -> str:
        return self.username
    
    def validate(self, username: str, password: str) -> bool:
        return username == self.username and password == self.password
    
    def display(self):
        while True:
            print(f"Hello {self.get_username()}")
            selection: str =""
            if self.access == "Admin":
                print("[A]dmin Panel\n[U]ser Panel\n[G]o Back\n[E]xit")
                selection = input()
                if selection not in "AUGE" or len(selection) != 1:
                    self.CONTROL.clear()
                    print("Wrong input please try again\n")
                    continue
                return selection
            else:
                return "U"
    
    def get_dictionary_info(self) -> dict:
            return {"username":self.username, "password": self.password, 
                    "name": self.name, "access": self.access}
            
    def query_on_username(self) -> dict:
        return {"username":self.username}