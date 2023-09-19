

import turtle
from turtle import *
t = Turtle()

t.shape("turtle")

def square (x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def turtlepyramid(x, rotation, length):
    def createrow(row):
        for i in range(row):
            square(length,rotation)
            t.forward(length)
        t.back(row*length)
        t.left(rotation)
        t.forward(length)
        t.right(rotation)
        t.forward(length)
    for i in range(x):
        createrow(x-i)
      

    
        
    
    
    
    
turtlepyramid(10,90,100)


turtle.done()