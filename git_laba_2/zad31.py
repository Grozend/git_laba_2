class User:
    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


class Employee(User):
    def set_age(self, age):
        if 18 < age < 65:
            self.age = age
        else:
            raise Exception("student name error")


employee = Employee()
employee.set_age(19)
print(employee.get_age())
