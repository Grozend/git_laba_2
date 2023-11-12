class User:
    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year


class Employee(User):
    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_sur(self, sur):
        self.sur = sur

    def get_sur(self):
        return self.sur


employee = Employee()

employee.set_salary(36000)
employee.set_name('Tom')
employee.set_sur('Antonovich')

print(employee.get_salary())
print(employee.get_name())
print(employee.get_sur())

employee.set_year(2014)
print(employee.get_year())




