from turtle import *
import random
penup()
speed(10)
goto(-140,140)
for step in range(9):
    write(step)
    right(90)
    fd(10)
    pendown()
    fd(200)
    penup()
    backward(210)
    left(90)
    fd(30)
t1=Turtle()
t1.penup()
t1.goto(0,-100)
t1.shape("turtle")
t1.color("blue")
t1.goto(-160,100)

t2=Turtle()
t2.penup()
t2.goto(0,-100)
t2.shape("turtle")
t2.color("red")
t2.goto(-160,50)

t3=Turtle()
t3.penup()
t3.goto(0,-100)
t3.shape("turtle")
t3.color("yellow")
t3.goto(-160,0)

t4=Turtle()
t4.penup()
t4.goto(0,-100)
t4.shape("turtle")
t4.color("green")
t4.goto(-160,-50)

for turn in range(108):
  t1.forward(random.randint(1,4))
  t1.pendown()
#for turn in range(110):
  t2.forward(random.randint(1,4))
  t2.pendown()
#for turn in range(110):
  t3.forward(random.randint(1,4))
  t3.pendown()
#for turn in range(110):
  t4.forward(random.randint(1,4))
  t4.pendown()




