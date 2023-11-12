class User:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.__enter_stri(self.name)

    def __enter_stri(self, stri):
        return stri


class Employee(User):
    def set_surn(self, surname):
        self.surname = surname

    def get_surn(self):
        return self.__enter_stri(self.surname)


employee = Employee()

print(employee.get_surn())  # AttributeError: 'Employee' object has no attribute '_Employee__enter_stri'
