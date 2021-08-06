from _datetime import datetime
from turtle import *


def desenharb(tartaruga):
    # bisel
    tartaruga.pensize(6)
    tartaruga.pencolor("black")
    tartaruga.goto(200, 0)
    tartaruga.pendown()
    tartaruga.circle(200)
    tartaruga.penup()


def desenharm(tartaruga):
    # marcadores
    tartaruga.pensize(3)
    tartaruga.goto(-182, 0)
    for i in range(12):
        tartaruga.penup()
        tartaruga.circle(-180, 360 / 12)
        tartaruga.pendown()
        tartaruga.dot()
    tartaruga.penup()


def desenharp(tartaruga, angulo, comprimento, largura, cor):
    # ponteiros
    tartaruga.home()
    tartaruga.pensize(largura)
    tartaruga.pencolor(cor)
    tartaruga.pendown()
    tartaruga.setheading(angulo)
    tartaruga.forward(comprimento)
    tartaruga.penup()


def main():
    mode("logo")
    #title("Relógio")
    tartaruga = Turtle()
    tartaruga.hideturtle()
    tartaruga.penup()
    tartaruga.speed(0)

    agora = datetime.now()
    #desenhar circulo
    desenharb(tartaruga)
    #desenhar horas - pontos
    desenharm(tartaruga)
    #desenhar ponteiro hora
    desenharp(tartaruga, agora.hour * 30, 100, 9, "black")
    # desenhar ponteiro min
    desenharp(tartaruga, agora.minute * 6, 150, 6, "black")
    # desenhar ponteiro seg
    desenharp(tartaruga, agora.second * 6, 175, 3, "red")
    done()


if (__name__ == "__main__"):
    main()