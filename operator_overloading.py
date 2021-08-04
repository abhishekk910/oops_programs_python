class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        a = self.x + self.y
        b = other.x + other.y
        return a+b
    def __gt__(self, other):
        a1 = (self.x**3)+(self.y**3)
        b1 = (other.x**3)+(other.y**3)
        return (a1 > b1)
p1 = Point(3,5)
p2 = Point(4,7)
p3 = Point(3,7)
print(p1 > p2)
print(p2 > p3)
print(p3 > p1)

