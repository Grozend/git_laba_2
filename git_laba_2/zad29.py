class User:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Employee(User):
    pass


employee = Employee()
employee.set_name('Tom')
print(employee.get_name())