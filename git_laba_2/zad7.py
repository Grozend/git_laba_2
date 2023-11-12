class Employee:
    name = None
    salary = None

    def return_name(self):
        print(self.name)

    def return_salary(self):
        print(self.salary)


employee = Employee()

employee.name = 'Anna'
employee.salary = 64000

employee.return_name()
employee.return_salary()
