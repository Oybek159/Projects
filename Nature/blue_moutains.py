import turtle

screen = turtle.Screen()
screen.setup(800, 400)
screen.bgcolor("#fff1e6")  # light beige background

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_triangle(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()
    pen.pendown()
    pen.goto(x + size / 2, y + size)
    pen.goto(x + size, y)
    pen.goto(x, y)
    pen.end_fill()

def draw_sun(x, y, radius, color):
    pen.penup()
    pen.goto(x, y - radius)
    pen.color(color)
    pen.begin_fill()
    pen.pendown()
    pen.circle(radius)
    pen.end_fill()

def draw_bird(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(90)
    pen.circle(100, 180)
    pen.circle(100, 180)

# Draw sun (behind mountains)
draw_sun(0, -20, 120, "#ff944d")

# Mountain layers (x, base y, size, color)
mountains = [
    [(-350, -100, 120, "#ccd9ff"), (-250, -100, 120, "#ccddff"), (-150, -100, 120, "#cce0ff"),
     (-50, -100, 120, "#ccddff"), (50, -100, 120, "#ccd9ff"), (150, -100, 120, "#ccddff"),
     (250, -100, 120, "#cce0ff")],

    [(-360, -150, 140, "#7ca6d6"), (-240, -150, 140, "#7ca6d6"), (-120, -150, 140, "#7ca6d6"),
     (0, -150, 140, "#7ca6d6"), (120, -150, 140, "#7ca6d6"), (240, -150, 140, "#7ca6d6")],

    [(-370, -200, 160, "#223f66"), (-210, -200, 160, "#1a365d"), (-50, -200, 160, "#102c54"),
     (110, -200, 160, "#0d274e"), (270, -200, 160, "#0a2044")]
]

# Draw all mountain triangles
for layer in mountains:
    for x, y, size, color in layer:
        draw_triangle(x, y, size, color)

# Draw birds
# draw_bird(x=-120, y=120)
# draw_bird(x=-90, y=140)
# draw_bird(x=-60, y=120)

pen.up()
pen.goto(-120, 120)
pen.down()
pen.setheading(90)
pen.circle(10, 180)
pen.setheading(90)
pen.circle(10, 180)

pen.up()
pen.goto(-90, 140)
pen.down()
pen.setheading(90)
pen.circle(10, 180)
pen.setheading(90)
pen.circle(10, 180)

pen.up()
pen.goto(-60, 120)
pen.down()
pen.setheading(90)
pen.circle(10, 180)
pen.setheading(90)
pen.circle(10, 180)

screen.mainloop()
