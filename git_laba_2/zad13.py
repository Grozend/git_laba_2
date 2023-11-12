class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def return_info(self):
        print(self.__name, self.__salary, self.__age)


employee = Employee('Ada', 89000, 18)

employee.return_info()
