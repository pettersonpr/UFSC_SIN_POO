# Importando Módulo
import turtle

t = turtle.Turtle()

t.pencolor('orange')
raio = 10
novoRaio = 0
aumentaRaio = 5

for i in range(1, 9):
    t.begin_fill()
    t.circle(raio)#######
    t.fillcolor('orange')
    t.end_fill()
    t.penup()
    novoRaio = raio + aumentaRaio
    if i == 8:
        t.forward(raio)
        break
    else:
        t.forward(raio + 1 + novoRaio)  #######
    raio = raio + aumentaRaio

turtle.done()