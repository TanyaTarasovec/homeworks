class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def triangle_ok(self):
        if self.a + self.b > self.c:
            return True
        else:
            return ValueError

    def is_right_angled(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        else:
            return False

    def perimetr(self):
        return self.a + self.b + self.c


t1 = Triangle(3, 4, 5)
t2 = Triangle(10, 10, 22)
t3 = Triangle(11, 11, 20)
print(t1.is_right_angled())
print(t2.triangle_ok())
print(t3.is_right_angled())
print(t1.perimetr())
