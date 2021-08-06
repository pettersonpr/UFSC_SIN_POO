import turtle

t = turtle.Turtle()

t.speed(100)

#fazer petala
circulo = 100
t.circle(circulo)
t.penup()
t.setposition(circulo*3/2, 0)
t.pendown()
t.circle(circulo)




turtle.done()
