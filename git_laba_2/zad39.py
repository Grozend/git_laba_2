class User:
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Employee(User):
    def set_sur(self, sur):
        self._sur = sur

    def get_sur(self):
        return self._sur


class Programmer(Employee):
    def set_skill_age(self, skill):
        self._skill = skill

    def get_skill_age(self):
        return self._skill


class Designer(Employee):
    def set_salary(self, salary):
        self._salary = salary

    def get_salary(self):
        return self._salary


designer = Designer()
programmer = Programmer()

designer.set_name('Anton')
designer.set_sur('Obramov')
designer.set_salary(34500)
programmer.set_skill_age(18)

print(designer.get_name(), designer.get_sur(), designer.get_salary(), programmer.get_skill_age())

'''
Сделайте класс Employee, который будет наследовать от класса User.

Сделайте класс Programmer, который будет наследовать от класса Employee.

Сделайте классы Designer, который будет наследовать от класса (Employee).

Добавьте в созданные вами классы различные методы.
'''