# use turtle to draw the following shape
# 1.
from turtle import *
# speed(0)
# for i in range(7):
#     color("grey")
#     forward(100)
#     left(360 / 7)
# for i in range(6):
#     color("yellow")
#     forward(100)
#     left(360 / 6)
# for i in range(5):
#     color("brown")
#     forward(100)
#     left(360 / 5)
# for i in range(4):
#     color("blue")
#     forward(100)
#     left(90)
# for i in range(3):
#     color("red")
#     forward(100)
#     left(120)

# 2.
from turtle import *
color("grey", "grey")

begin_fill()
for i in range(2):
    forward(250)
    left(90)
    forward(100)
    left(90)
end_fill()

color("yellow", "yellow")

begin_fill()
for i in range(2):
    forward(200)
    left(90)
    forward(100)
    left(90)
end_fill()

color("brown", "brown")

begin_fill()
for i in range(2):
    forward(150)
    left(90)
    forward(100)
    left(90)
end_fill()

color("blue", "blue")

begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(100)
    left(90)
end_fill()

color("red")

begin_fill()
for i in range(2):
    forward(50)
    left(90)
    forward(100)
    left(90)
end_fill()



mainloop()