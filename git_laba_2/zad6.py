class Employee:
    def try_pass(self, name, salary):
        return name + ' - ' + salary


employee = Employee()

print(employee.try_pass('Marta', '35000'))