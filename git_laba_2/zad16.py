class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_age(self):
        return self.__age


employee = Employee('Bodrost', 12000, 18)
print(employee.get_name())
print(employee.get_salary())
print(employee.get_age())