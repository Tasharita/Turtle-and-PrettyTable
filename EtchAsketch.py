import turtle as t

draw = t.Turtle()
draw.shape("arrow")
t.listen()

def move_forward():
    draw.forward(10)
def move_backward():
    draw.backward(10)
def move_counterclockwise(): #turn left
    draw.left(10)
def move_clockwise(): #turn right
    draw.right(10)
def clear_screen():
    draw.home()
    draw.clear()


t.onkey(key = "w", fun = move_forward)
t.onkey(key = "s", fun = move_backward)
t.onkey(key = "a", fun = move_counterclockwise)
t.onkey(key = "d", fun = move_clockwise)
t.onkey(key = "c", fun = clear_screen)

screen = t.Screen()
screen.exitonclick()