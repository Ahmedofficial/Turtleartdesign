

from turtle import * 
                   

speed(0) 
pencolor('red')
bgcolor('black') 
x = 0 
up() 



right(45) 
forward(90) 
right(135) 

down() 
while x < 100: 
    
    
    forward(200)     
    right(61)
    forward(200)
    right(61)
    forward(200)
    right(61)
    forward(200)
    right(61)
    forward(200)
    right(61)
    forward(200)
    right(61)
   
    right(11.11) 
    x = x+1


import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
Will= turtle.Turtle()
Will.speed(0)
Will.color('silver')
rotate=int(360)

def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
        
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Will,100,10)
Will= turtle.Turtle()
Will.speed(0)
Will.color('light blue')
rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
        
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
        
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Will,100,10)
Will = turtle.Turtle()
Will.speed(0)
Will.color('orange')
rotate=int(90)

def drawCircles(t,size):
    for i in range(4):
        Will.circle(size)
        size=size-5

        
import turtle 
bob=turtle.Turtle()
bob.speed(0)
def flower(t):
    for times in range(40):
        t.home()
        t.left(times * 32)
        petal(t, 45  - times)
        t.forward(times + 10)







