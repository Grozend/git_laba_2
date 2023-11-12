class User:
    def __init__(self):
        self.age = None

    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception('need age more 0')

    def get_age(self):
        return self.age


class Employee(User):
    def set_age(self, age):
        if age <= 120:
            super().set_age(age)
        else:
            raise Exception('need age less 120')


employee = Employee()
employee.set_age(29)
print(employee.get_age())