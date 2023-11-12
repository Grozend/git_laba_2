class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getSalary(self):
        return self.__addSign(self.__salary)

    def __addSign(self, num): # приватный метод
        return num + '$'


employee = Employee('Bodrost', '12000')
print(employee.getSalary())
