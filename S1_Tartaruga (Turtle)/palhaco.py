# Importando Módulo
import turtle

t = turtle.Turtle()


def circuloPreto(tCirculo):
    t.begin_fill()
    t.fillcolor('black')
    t.circle(tCirculo)
    t.end_fill()


def circuloAzul(tCirculo):
    t.pencolor('blue')
    for i in [1, 3/2, 4/2]:
        t.circle(tCirculo*i)
    t.pencolor('black')

#circulo preto
t.left(90)
circuloPreto(30)#Lado Esquerdo
circuloAzul(50)#Lado Direito
t.left(180)
circuloPreto(30)#Lado Esquerdo
circuloAzul(50)#Lado Direito

#nariz
t.penup()
t.setposition(0, -180)
t.pendown()
t.pencolor('pink')
for i in range(30):
    t.forward(50)
    t.setposition(0, -180)
    t.backward(50)
    t.setposition(0, -180)
    t.left(6)

#Boca
t.penup()
t.right(180-30)
t.setposition(-80,-250)
t.pendown()
t.pensize(5)
t.pencolor('red')
t.circle(100, 120)

turtle.done()