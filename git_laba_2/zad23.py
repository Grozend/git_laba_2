class Employee:
    name = None

    def __init__(self, name):
        self.name = name


class Position:
    posotion = None

    def __init__(self, position):
        self.posotion = position


class Department:
    department = None

    def __init__(self, department):
        self.department = department


class User:
    name = None
    position = None
    department = None

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department


name = Employee('Pasha')
position = Position('Glava')
department = Department('Minzdrav')
user = User(name, position, department)

print(user.name.name)
print(user.position.posotion)
print(user.department.department)