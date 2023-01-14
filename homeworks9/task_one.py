class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        try:
            self.a + self.b > self.c
        except ValueError:
            raise ValueError

    def is_right_angled(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Triangle):
            return (self.a + self.b + self.c == other.a + other.b + other.c)              
        return False


t1 = Triangle(3, 4, 5)
t2 = Triangle(10, 10, 22)
t3 = Triangle(11, 11, 20)
print(t1.is_right_angled())
print(t3.is_right_angled())
print(t3 == t1)
