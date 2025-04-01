import random
from turtle import *

bob = Turtle()
colormode(255)
bob.shape("triangle")
bob.speed("fastest")

def random_color():
    """Returns a random RGB color"""
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour


# draws a square
for _ in range(4):
    bob.backward(100)
    bob.left(90)

# draws a dashed line
for _ in range(15):
    bob.backward(10)
    bob.penup()
    bob.backward(10)
    bob.pendown()

# draw different shapes from triangle to decagon
def draw(num_sides):
    """Draws the shapes depending on the angle"""
    angle = 360 / num_sides
    for _ in range(num_sides):
        bob.forward(100)
        bob.right(angle)

for n in range(3,11):
    bob.color(random_color())
    draw(n)

# draw a random walk
bob.width(5)
directions = [0, 90, 180, 270]

for _ in range(200):
    bob.color(random_color())
    bob.forward(30)
    bob.setheading(random.choice(directions))

#draw a spirograph
def draw_spirograph(size_of_gap):
    """draws a spirograph and stops once it's done ie no overlapping"""
    for _ in range(int(360/size_of_gap)):
        bob.setheading(bob.heading() + size_of_gap)
        bob.color(random_color())
        bob.circle(100)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()