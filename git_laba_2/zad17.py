class Employee:
    __name = None
    __salary = None
    __age = None

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def set_age(self, age):
        self.__age = age


employee = Employee()

employee.set_name('Yan')
employee.set_salary('120900')
employee.set_age('23')

print(employee.get_name())
print(employee.get_salary())
print(employee.get_age())