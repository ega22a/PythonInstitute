import turtle, random

turtle.bgcolor("white")
turtle.reset()
turtle.color("red", "black")
for i in range(0, 100):
    turtle.begin_fill()
    turtle.circle(random.randint(10, 100))
    turtle.end_fill()
    turtle.up()
    turtle.goto(random.randint(-800, 800), random.randint(-600, 600))
    turtle.down()