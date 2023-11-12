class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def return_name(self):
        return self.name

    def return_salary(self):
        return self.salary

    def return_percent_salary(self):
        return self.salary * 0.1 + self.salary


employee = Employee('Ada', 89000)

print(employee.return_name())
print(employee.return_salary())
print(employee.return_percent_salary())