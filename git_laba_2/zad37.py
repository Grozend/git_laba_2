class User:
    def set_name(self, name):
        if self._not_empty(name):
            self.name = name

    def get_name(self):
        return self._not_empty(self.name)

    def _not_empty(self, stri):
        return len(stri) > 0


class Employee(User):
    def set_surn(self, surname):
        if self._not_empty(surname):
            self.surname = surname

    def get_surn(self):
        return self._not_empty(self.surname)


employee = Employee()

employee.set_name('John')
employee.set_surn('Bagachev')

print(employee.get_name(), employee.get_surn())