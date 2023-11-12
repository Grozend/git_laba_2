class Student:
    name = 'Fallen'
    surname = 'Senned'

    def show(self):
        return self.name, self.surname

student = Student()

print(student.name, student.surname)