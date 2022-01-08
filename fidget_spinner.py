from turtle import *
turn=0
tracer(False)
title('Fidget Spinner')
setup(600,600,0,0)
width(50)
tracer(False)
left(30)


color = ['red', 'yellow', 'green','orange','gray','blue']
def Draw(color = ['red', 'yellow', 'green','orange','gray','blue']):
  clear()
  right(turn/10) 
  for i in range(6):
    forward(200)
    dot(170, color[i])
    dot(100,'white')
    penup()
    backward(200)
    right(60)
    pendown()
  update()
    


def animate():
  global turn
  if turn > 0:
    turn = turn - 1
  Draw(color)
  ontimer(animate, 20)

def flick():
  global turn
  turn = turn + 10
  
  

onkey(flick,'space')

listen()

animate()