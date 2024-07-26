from Menu import Menu 

class StoreMenu(Menu):
    def __init__(self, name: str = "General"):
        super().__init__(name)
    
    def display(self):
        while True:
            print(f"Welcome To {self.object} store")
            selection: str = input("[L]ogin\n[C]reate Account\n[E]xit\n")
            if selection not in "LE" or len(selection) != 1:
                print("Wrong input please try again")
                print()
                continue
            match selection:
                case "L":
                    print()    
                    username: str = input("Username: ")
                    passowrd: str = input("Password: ")
                    break
                case "E":
                    self.CONTROL.clear()
                    return