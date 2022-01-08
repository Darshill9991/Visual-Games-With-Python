import time
from random import *
from turtle import *
from freegames import vector

bird = vector(0, 0)
balls = []
screen_size = 600
score = 0

def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)

def move_left():
    "Move bird up in response to screen tap."
    left = vector(-10, 0)
    bird.move(left)

def move_right():
    "Move bird up in response to screen tap."
    right = vector(10, 0)
    bird.move(right)

def move_up():
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)

def inside(point):
    "Return True if point on screen."
    return -screen_size/2 <= point.x <= screen_size/2 and -screen_size/2 <= point.y <= screen_size/2

def draw(alive):
    "Draw screen objects."
    clear()

    # goto(bird.x, bird.y)
    bird_.goto(bird.x, bird.y)


    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()

def move():
    global score
    pen.goto(0, 270)
    pen.clear()
    pen.write("Score: " + str(score), align="center", font=("Courier", 24, "normal"))
    score += 1
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-screen_size/2, screen_size/2)
        ball = vector(screen_size/2, y)
        print(ball)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 25:
            draw(False)
            return
            

    draw(True)
    ontimer(move, 50)

bgpic('background.gif')
register_shape('b2.gif')

bird_ = Turtle()
pen = Turtle()
# bird_.s = 'b2.gif'
bird_.shape('b2.gif')
bird_.up()

setup(screen_size, screen_size)
hideturtle()
up()
tracer(False)
# onscreenclick(tap)
onkey(move_left,'Left')
onkey(move_right,'Right')
onkey(move_up,'Up')

listen()
time.sleep(5)
move()
done()