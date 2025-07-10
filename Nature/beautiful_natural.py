import turtle

screen = turtle.Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def draw_polygon(points, color):
    pen.penup()
    pen.goto(points[0])
    pen.color(color)
    pen.begin_fill()
    pen.pendown()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()


draw_polygon([(-400, 0), (-400, 250), (400, 250), (400, 0)], "red")


pen.penup()
pen.goto(150, 30)
pen.setheading(0)
pen.color("yellow")
pen.begin_fill()
pen.circle(75)
pen.end_fill()


draw_polygon([(-400, 0), (-400, -250), (400, -250), (400, 0)], "#0a082b")

pen.penup()
pen.goto(150, -180)
pen.setheading(0)
pen.color("#888d38")
pen.begin_fill()
pen.circle(75)
pen.end_fill()


draw_polygon([(-400, 0),(-250, -150),(-100, -90),(0, -250),(150, -50),(250, -180),(400, 0)], "#5a3d1c")

draw_polygon([(-400, 0),(-250, 150),(-100, 90),(0, 250),(150, 50),(250, 180),(400, 0)], "darkorange")

screen.mainloop()
