class Rectangle:
    widthr = None
    hightr = None

    def get_square(self):
        return self.widthr * self.hightr

    def get_perimetr(self):
        return (self.widthr * 2) + (self.hightr * 2)

    def get_ratio(self):
        return self.get_square() / self.get_perimetr()
    

rect = Rectangle()

rect.widthr = 18
rect.hightr = 12

print(rect.get_square())
print(rect.get_perimetr())
print(rect.get_ratio())

