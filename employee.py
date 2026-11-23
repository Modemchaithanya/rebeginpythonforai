class employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def display_name(self):
        print(f"Employee name: {self.name}")

    def display_age(self):
        print(f"Employee age: {self.age}")

    def display_salary(self):
        print(f"Employee salary: {self.salary}")
