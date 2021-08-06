import turtle

t = turtle.Turtle()

# Tamanho caneta
t.pensize(3)
# Circulo
t.circle(100)
# Referencia
t.penup()
t.goto(0, 20)
t.pendown()
t.pensize(2)
for i in range(12):
    t.penup()
    t.circle(80, 360 / 12)
    t.pendown()
    t.dot()
t.penup()
# Caneta no meio do ponteiro
t.goto(0, 100)

def ponteiro (cor, comprimento, angulo, espessura):
    t.left(angulo)
    t.pencolor(cor)
    t.pensize(espessura)
    t.pendown()
    t.forward(comprimento)
    t.penup
    t.backward(comprimento)
    t.right(angulo)
# Ponteiro segundos
ponteiro('red', 80, 97, 2)
# Ponteiro Minutos
ponteiro('black', 65, 10, 3)
# Ponteiro Horas
ponteiro('black', 35, 160, 5)

turtle.done()
