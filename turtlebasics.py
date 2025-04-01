import turtle as t #t is the alias

timmy = t.Turtle() #forms the object
print(timmy) #prints the object
timmy.shape("turtle") #changes shape of object to turtle
timmy.color("coral") #changes color of object
timmy.forward(100)#makes the object move forward by 100 spaces

my_screen = t.Screen() #creates the screen
print(my_screen.canvheight)#return height of the window
my_screen.exitonclick() #allow screen to exit when you click