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


# draw first circles
n = 1
while n <= 10:
    # t1.speed(n)
    # t2.speed(n)
    
    t1.circle(n ** 2)
    t2.circle(n ** 2)
    n += 1
    
# t1.speed(10)
# t2.speed(10)

t1.pencolor("yellow")
t2.pencolor("green")

t1.forward(100)
t2.forward(100)

# draw squares around circles
for i in range(1, 4):
    t1.left(90)
    t2.left(90)
    
    t1.forward(200)
    t2.forward(200)

t1.pencolor("crimson")
t2.pencolor("wheat")

# draw triangles "around" squares
t1.right(45)    
t2.right(45)
    
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

# prepare to draw flowers, slight adjustment to center them
t1.forward(90)
t2.forward(90)

t1.right(90)
t2.right(90)

t1.forward(4)
t2.forward(4)

t1.left(90)
t2.left(90)

# draw flowers
for i in range(0, 38):
    t1.forward(100)
    t1.left(170)
    
    t2.forward(100)
    t2.left(170)
    
    if abs(t1.pos()) < 1 or abs (t2.pos()) < 1:
        break


# prepare to draw circles around flowers
t1.penup()
t2.penup()

t1.goto(-51, -220)
t2.goto(51, 220)

t1.pendown()
t2.pendown()

t1.pencolor("white")
t2.pencolor("blue")

# draw circles
t1.circle(55)
t2.circle(55)

# prepare to draw large squares around art piece
t1.penup()
t2.penup()

t1.goto(-200, -300)
t2.goto(200, 300)

t1.left(20)
t2.left(20)

t1.pendown()
t2.pendown()

t1.pencolor("green")
t2.pencolor("pink")

# draw small squares
for i in range(0, 4):
    t1.left(90)
    t2.left(90)
    
    t1.forward(400)
    t2.forward(400)
    

t1.pencolor("brown")
t2.pencolor("yellow")

# draw squares
for i in range(0, 4):
    t1.right(90)
    t2.right(90)
    
    t1.forward(400)
    t2.forward(400)
    
t1.pencolor("grey")
t2.pencolor("red")
    
# prepare to draw square pattern
t1.penup()
t2.penup()

t1.right(90)
t1.forward(200)
t1.right(90)
t1.forward(200)

t2.right(90)
t2.forward(200)
t2.right(90)
t2.forward(200)

t1.pendown()
t2.pendown()

# draw square pattern
n = 0
while n <= 396:
    
    
    if n % 10 == 0:
        t1.pencolor("orange")
        t2.pencolor("blue")
    elif n % 10 == 4 or n % 10 == 2:
        t1.pencolor("green")
        t2.pencolor("yellow")
    elif n % 10 == 8 or n % 10 == 6:
        t1.pencolor("purple")
        t2.pencolor("red")
    
    t1.forward(n)
    t2.forward(n)
    
    t1.right(90)
    t2.right(90)
    n += 4
    
# prepare to draw rectangles + triangles
t1.penup()
t2.penup()

t1.right(90)
t2.right(90)

t1.forward(798)
t2.forward(798)

t1.pendown()
t2.pendown()

# draw triangles
t1.left(26)
t2.left(26)

t1.forward(451)
t2.forward(451)

t1.left(64)
t2.left(64)

# draw rectangles
for i in range(0, 4):
    t1.left(90)
    t2.left(90)
    
    if i % 2 == 0:
        t1.forward(400)
        t2.forward(400)
    else:
        t1.forward(200)
        t2.forward(200)
    

turtle.done()
