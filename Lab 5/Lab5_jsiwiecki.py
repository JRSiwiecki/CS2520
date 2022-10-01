# Author: Joseph Siwiecki
# Assignment: Lab 5
# Completed: 10/1/2022
# Class: CS 2520.01

import turtle

# --------------------- TASK 1 ---------------------

# initialize screen with turtle
# initialize turtle
screen = turtle.getscreen()

t1 = turtle.Turtle()
t2 = t1.clone()

turtle.title("Lab 5 - JSiwiecki")
turtle.bgcolor("black")

t1.pencolor("aquamarine")
t2.pencolor("magenta")

t1.speed(0)
t2.speed(0)

t1.right(90)
t2.left(90)

n = 1
while n <= 10:
    # t1.speed(n)
    # t2.speed(n)
    
    t1.circle(n ** 2)
    t2.circle(n ** 2)
    n += 1
    
t1.speed(10)
t2.speed(10)
    
t1.pencolor("yellow")
t2.pencolor("green")

t1.forward(100)
t2.forward(100)

for i in range(1, 4):
    t1.left(90)
    t2.left(90)
    
    t1.forward(200)
    t2.forward(200)

t1.pencolor("crimson")
t2.pencolor("wheat")

t1.speed(8)
t2.speed(8)

t1.right(90)
t2.right(90)

t1.left(45)    
t2.left(45)
    
t1.forward(283)
t2.forward(283)

t1.left(135)
t2.left(135)

t1.forward(600)
t2.forward(600)

t1.left(135)
t2.left(135)

t1.forward(283)
t2.forward(283)

t1.right(135)
t2.right(135)

t1.pencolor("gold")
t2.pencolor("pink")

t1.forward(42)
t2.forward(42)

t1.right(90)
t2.right(90)

t1.circle(100)
t2.circle(100)  

turtle.done()
