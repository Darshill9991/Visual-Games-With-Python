from random import *
from turtle import *
from freegames import floor, vector
'''
freegames.floor(value, size, offset=200)

The floor function is best understood with a diagram of the number line:
-200  -100    0    100   200
<--|--x--|-----|--y--|--z--|-->

The number line shown has offset 200 denoted by the left-hand tick mark at -200 and size 100 denoted by the tick marks at -100, 0, 100, and 200. The floor of a value is the left-hand tick mark of the range where it lies. So for the points show above: floor(x) is -200, floor(y) is 0, and floor(z) is 100.
floor(10, 100)
>> 0.0
floor(120, 100)
>> 100.0
floor(-10, 100)
>> -100.0
floor(-150, 100)
>> -200.0
floor(50, 167)
>> -33.0

class freegames.vector(x, y)

Two-dimensional vector.
Vectors can be modified in-place.

v = vector(0, 1)
v.move(1)
v
>>vector(1, 2)
v.rotate(90)
v
>>vector(-2.0, 1.0)

'''
tiles = {}
neighbors = [
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100),
]

def load():
  "Load tiles and scramble."
  count = 1

  "This is where we fill the tiles sequentially from 1 to 15"
  for y in range(-200, 200, 100):
    for x in range(-200, 200, 100):
      mark = vector(x, y)
      tiles[mark] = count
      count += 1

  tiles[mark] = None

  '''
  {
  vector(-200, -200): 1, 
  vector(-100, -200): 2, 
  vector(0, -200): 3, 
  vector(100, -200): 4, 
  vector(-200, -100): 5, 
  vector(-100, -100): 6, 
  vector(0, -100): 7, 
  vector(100, -100): 8, 
  vector(-200, 0): 9, 
  vector(-100, 0): 10, 
  vector(0, 0): 11,
  vector(100, 0): 12, 
  vector(-200, 100): 13, 
  vector(-100, 100): 14, 
  vector(0, 100): 15, 
  vector(100, 100): None
  }
  '''

  'We will randomize the numbers now'
  for count in range(1000):
    neighbor = choice(neighbors)
    spot = mark + neighbor

    if spot in tiles:
      number = tiles[spot]
      tiles[spot] = None
      tiles[mark] = number
      mark = spot
      

def square(mark, number):
    "Draw white square with black outline and number."
    up()
    goto(mark.x, mark.y)
    down()

    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(99)
        left(90)
    end_fill()

    if number is None:
        return
    elif number < 10:
        forward(35)

    write(number, font=('Arial', 60, 'normal'))

def tap(x, y):
    "Swap tile and empty square."
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)

    for neighbor in neighbors:
        spot = mark + neighbor

        if spot in tiles and tiles[spot] is None:
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)

def draw():
    "Draw all tiles."
    for mark in tiles:
        square(mark, tiles[mark])
    update()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
load()
draw()
onscreenclick(tap)
done()