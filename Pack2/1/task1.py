#! /usr/bin/python3

class Vector :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"<{self.x}; {self.y}>"
    def __repr__(self):
        return f"<{self.x}; {self.y}>"


    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __len__(self):
        return abs(int(abs(self))) 

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)
    def __rmul__(self, value):
        return Vector(self.x * value, self.y * value)
    def __imul__(self, value):
        self.x *= value
        self.y *= value
        return self
    def __irmul__(self, value):
        self.x *= value
        self.y *= value
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

if __name__ == "__main__":
    v1 = Vector(3,4)
    v2 = Vector(5,7)
    v3 = v1

    print(v1, v2, v3)
    print("v1 + v2: ", v1 + v2)
    print("v1 - v2: ", v1 - v2)
    print("abs(v1): ", abs(v1))
    print("len(v1): ", len(v1))

    print("v1 * 5: ", v1 * 5)
    print("v1 == v2: ", v1 == v2)
    print("v1 == v3: ", v1 == v3)



