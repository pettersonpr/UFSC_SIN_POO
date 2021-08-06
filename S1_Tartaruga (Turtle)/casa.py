import turtle
import math

t = turtle.Turtle()

x = 100


# Desenhando parede da casa
def parede(t, x):
    t.begin_fill()
    for i in range(2):
        t.forward(2 * x)
        t.left(90)
        t.forward(x)
        t.left(90)
    t.fillcolor(('red'))
    t.end_fill()


# Porta
def porta(t, x):
    t.forward(x / 3)
    t.left(90)
    t.begin_fill()
    t.fillcolor('blue')
    t.forward(2 * x / 3)
    t.right(90)
    t.forward(x / 3)
    t.right(90)
    t.forward(2 * x / 3)
    t.left(90)
    t.end_fill()


def QuadradoColorido(t, cor):
    """Quadrado de lado 100"""
    t.begin_fill()
    t.fillcolor(cor)
    for desenhando in range(4):
        t.forward(4 * x / 15)
        t.right(90)
    t.end_fill()


# Janela
def janela(t, x):
    # t.forward(x/3)
    t.forward(4 * x / 15)
    t.left(90)
    t.penup()
    t.forward(x / 3)
    t.pendown()
    # t.begin_fill()
    # t.fillcolor('yellow')

    QuadradoColorido(t, 'yellow')
    t.right(90)
    t.penup()
    t.forward(2 * (4 * x / 15))
    t.pendown()
    t.left(90)
    QuadradoColorido(t, 'yellow')


# Telhado
def telhado(t, x):
    t.penup()
    t.forward(2 * x / 3)
    t.right(90)
    # t.forward(2*x/3)
    t.forward(2 * (4 * x / 15))
    t.left(135)
    t.pendown()
    t.begin_fill()
    t.fillcolor('green')
    t.forward(x * math.sqrt(2))
    t.left(90)
    t.forward(x * math.sqrt(2))
    t.end_fill()


def beirasTelhado():
    t.forward(x / 5)
    t.left(180)
    t.forward(x / 5)
    t.right(45)
    t.penup()
    t.forward(2 * x)
    t.right(45)
    t.pendown()
    t.forward(x / 5)
    t.penup()
    t.right(45)
    t.forward(x)


parede(t, x)
porta(t, x)
janela(t, x)
telhado(t, x)
beirasTelhado()

turtle.done()
