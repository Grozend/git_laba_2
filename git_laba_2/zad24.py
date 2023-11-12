class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary


employees = [
            Employee('Anna', 32500),
            Employee('Sasha', 120500),
            Employee('Masha', 135900)
]

for employee in employees:
    print(employee.get_name(), employee.get_salary())
