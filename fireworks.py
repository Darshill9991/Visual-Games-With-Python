import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(200)

screen.colormode(255)

for i in range(15):
  x = random.randint(-250, 250)
  y = random.randint(-250,250)
  t.penup()
  t.goto(x,y)
  t.pendown()

  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  t.pencolor(r,g,b)

  size = random.randint(30, 150)
  for i in range(36):
    t.forward(size)
    t.backward(size)
    t.left(10)
