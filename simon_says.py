from random import choice
from time import sleep
from turtle import *
from freegames import floor, square, vector

pattern = []
guesses = []
tiles = {
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('cyan', 'sky blue'),
    vector(-200, 0): ('light green', 'green'),
    vector(-200, -200): ('yellow', 'gold'),
}

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

------------------
freegames.square(x, y, size, name)

Draw square at (x, y) with side length size and fill color name.
The square is oriented so the bottom left corner is at (x, y).

-----------------
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


Again you see, tiles is a dictionary, whose key is a vector and value is a tuple. 

A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.

'''

def grid():
    "Draw grid of tiles."
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'sky blue')
    square(-200, 0, 200, 'green')
    square(-200, -200, 200, 'gold')
    update()

def flash(tile):
    "Flash tile in grid."
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    sleep(0.5)
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(0.5)

def grow():
    "Grow pattern and flash tiles."
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()

def tap(x, y):
    "Respond to screen tap."
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        exit()

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()

    onscreenclick(tap)

def start(x, y):
    "Start game."
    grow()
    onscreenclick(tap)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(start)
done()