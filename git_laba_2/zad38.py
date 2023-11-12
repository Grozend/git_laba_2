class User:
    _name = None

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Employee(User):
    def inc_name(self):
        if len(self._name) > 0:
            self._name = self._name


employee = Employee()

employee.set_name('Vasya')
print(employee.get_name())
