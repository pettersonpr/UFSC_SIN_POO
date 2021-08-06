import turtle

t = turtle.Turtle()

t.speed(0)
angulo = 360 / 7

# Desenhar Pétalas
for i in range(7):
    t.begin_fill()
    t.fillcolor('pink')
    t.circle(100, 90)
    t.left(90)
    t.circle(100, 90)
    t.end_fill()
    t.setheading(0)  # Reposicionando rotação
    t.right(angulo)
    angulo = angulo + (360 / 7)

# Desenhar Caule
t.setheading(270)  # Reposicionando rotação
t.pensize(6)
t.pencolor('green')
t.forward(300)

# Desenhar folha do caule
t.backward(100)
t.setheading(0)  # Reposicionando rotação
t.pensize(1)
t.begin_fill()
t.fillcolor('green')
t.circle(50, 90)
t.left(90)
t.circle(50, 90)
t.end_fill()

turtle.done()
