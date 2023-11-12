class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def get_surn(self):
        return self.surname


class Employee(User):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname)
        self.age = age
        self.salary = salary

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary


employee = Employee('Boria', 'Vasnetsov', 18, 235000)

print(employee.get_name(), employee.get_surn(), employee.get_age(), employee.get_salary())
