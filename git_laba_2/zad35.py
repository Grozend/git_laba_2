class User:
    __name = None
    __surname = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_surn(self, surname):
        self.__surname = surname

    def get_surn(self):
        return self.__surname

    def get_full(self):
        return self.__name + ' ' + self.__surname


class Employee(User):
    pass


employee = Employee()

employee.set_name('Bonia')
employee.set_surn('Vasilkov')

name = employee.get_name()
surn = employee.get_surn()

print(employee.get_full())
print(name, surn)