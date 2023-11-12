class User:
    __name = 'a'

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Employee(User):
    __name = 'a'

    def __init__(self):
        __name = self.get_name()

    def set_name(self, name):
        if len(name) > 0:
            self.__name = name


employee = Employee()
employee.set_name('Yry')
print(employee.get_name())
