#! /usr/bin/python3

import math
from abc import abstractmethod

class BaseF:
    @abstractmethod
    def sqare(self):
        pass   

class Rectangle(BaseF) :
    name = "Rectangle"
    def __init__(self, l, h):
        self.l = l
        self.h = h
    def square(self):
        return self.l * self.h

class Triangle(BaseF) :
    name = "Triangle"
    def __init__(self, h, hside):
        self.h = h
        self.hside = hside
    def square(self):
        return (self.h * self.hside) / 2

class Circle(BaseF) :
    name = "Circle"
    def __init__(self, radius):
        self.radius = radius
    def square(self):
        return (math.pi * ( self.radius ** 2 ))

if __name__ == "__main__":
    
    a = Rectangle(3,4)
    print(a.name, a.square())
    
    b = Triangle(3,4)
    print(b.name, b.square())

    c = Circle(5)
    print(c.name, c.square())


