class Person:
    def __init__(self, name: str, age: int, salary: float = None):
        self.name = name.title()
        self.age = age
        self.salary = salary
    
    def change_salary(self, ammount: float) -> None:
        self.salary = ammount
    
    def get_dictionary_info(self) -> dict:
        if self.salary is None:
            return {"name":self.name, "age": self.age}
        return {"name":self.name, "age": self.age,"salary": self.salary}