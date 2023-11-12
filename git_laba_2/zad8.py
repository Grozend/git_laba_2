class Student:
    name = 'astro'
    surname = 'momuate'

    def initials(self):
        return self.case_up(self.name[0], self.surname[0])

    def case_up(self, stri1, stri2):
        return stri1.upper() + ' ' + stri2.upper()


student = Student()

print(student.initials())
