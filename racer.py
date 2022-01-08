#!/bin/python3

from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)


def create_turtles(color,shape):
  turtle = Turtle()
  turtle.color(color)
  turtle.shape(shape)
  turtle.penup()
  turtle.goto(-160, 100)
  turtle.pendown()
  return turtle

ada = create_turtles(color = 'red', shape = 'turtle')

for turn in range(10):
  ada.right(36)

bob = create_turtles(color = 'blue', shape = 'turtle')

for turn in range(72):
  bob.left(5)

ivy = create_turtles(color = 'green', shape = 'turtle')

for turn in range(60):
  ivy.right(6)

jim = create_turtles(color = 'orange', shape = 'turtle')

for turn in range(30):
  jim.left(12)

finish_line = 140

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  ivy.forward(randint(1,5))
  jim.forward(randint(1,5))

  if ada.pos()[0] >=140:
    winner = 'Ada'
    for turn in range(30):
      ada.left(12)
  elif bob.pos()[0] >=140:
    winner = 'Bob'
    for turn in range(30):
      bob.left(12)
  elif ivy.pos()[0] >=140:
    winner = 'Ivy'
    for turn in range(30):
      ivy.left(12)
  elif jim.pos()[0] >=140:
    winner = 'Jim'
    for turn in range(30):
      jim.left(12)

pen = Turtle()  
pen.goto(0, 265)
# pen.clear()
pen.write(winner + " WINSS!!", align="center", font=("Courier", 24, "normal"))



print(ada.pos(),bob.pos(),ivy.pos(),jim.pos())  