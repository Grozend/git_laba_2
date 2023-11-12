class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary


class EmployeeCollection:

    def __init__(self):
        self.__employees = []

    def add(self, employee):
        self.__employees.append(employee)

    def show(self):
        for employee in self.__employees:
            print(employee.get_name(), employee.get_salary())

    def show_sum_salary(self):
        summ = 0
        for employee in self.__employees:
            summ += employee.get_salary()
        return summ

    def show_avg_salary(self):
        avg = self.show_sum_salary()
        if len(self.__employees) > 0:
            avg = avg / len(self.__employees)
            return avg
        else:
            return 0


ec = EmployeeCollection()

ec.add(Employee('Ann', 123700))
ec.add(Employee('Petr', 23200))
ec.add(Employee('Luna', 54800))

ec.show()
print(ec.show_sum_salary())
print(ec.show_avg_salary())