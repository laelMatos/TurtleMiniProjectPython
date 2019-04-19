import random
import turtle

janela = turtle.Screen()
janela.bgcolor('lightblue')

#inicio circulos de fundo.

def circulos():
    c = turtle.Turtle()
    for i in range(100):
        c.speed(0.05)
        c.pu()
        c.setpos(random.randrange(-400,400,10),random.randrange(-400,400,10))
        c.pd()
        c.color(random.choice(['#4b9bbe','#6db0cb','#ae0fa9','#9ba4cd','#a5c0dd','#27618f']))
        c.begin_fill()
        c.dot(random.randint(5,80))
        c.end_fill()
        c.hideturtle()

circulos()
#Fim circulos

#Inicio flor
def petala(g,comp,angulo): #petalas/folhas
    for i in range(4):
        g.forward(comp)
        g.left(180 - angulo)
        g.forward(comp)
        g.left(angulo)
        g.hideturtle()

def folha (f):
    for i in range(2):
        f.circle(100,100)
        f.left(80)
        f.hideturtle()

def corpo(x,y):
    li = turtle.Turtle()
    li.speed(0)
    li.pu()
    li.setpos(x,y)
    li.pd()

    #talo
    li.color('brown')
    li.width(10)
    li.right(90)
    li.forward(400)
    #end talo

    li.pu()
    li.setpos(x,y)
    li.pd()
    li.width(1)

    #petalas
    for i in range(72):
        li.color('red','pink')
        li.begin_fill()
        petala(li,90,160)
        li.right(5)
        li.end_fill()
        li.hideturtle()

    #botão flor
    li.color('yellow')
    li.dot(60)

    #folhas
    li.pu()
    li.setpos(x,y)
    li.forward(300)
    li.pd()
    li.color('green')
    li.begin_fill()
    li.right(180)
    folha(li)
    li.right(100)
    folha(li)
    li.end_fill()
    li.hideturtle()

corpo(-100,-70)
#end flor

def letras(x,y):
    la = turtle.Turtle()
    la.width(10)
    la.color('white')

    #letra 'L'
    for i in range(2):
        if i == 1:
            i = 350
        la.pu()
        la.setpos(x+i,y)
        la.pd()
        la.right(90)
        la.forward(150)
        la.left(90)
        la.forward(70)

    #letra 'A'
    la.pu()
    la.setpos(x + 100, y - 150)
    la.pd()
    la.left(75)
    la.forward(150)
    la.right(150)
    la.forward(150)

    la.pu()
    la.setpos(x + 115, y - 100)
    la.pd()
    la.left(75)
    la.forward(50)

    #Letra 'E'
    la.pu()
    la.setpos(x + 300, y - 150)
    la.pd()
    la.forward(-70)
    la.left(90)
    la.forward(150)
    la.right(90)
    la.forward(70)

    la.pu()
    la.setpos(x + 300, y - 75)
    la.pd()
    la.forward(-70)

    la.hideturtle()

letras(-400, 350)

#fractal
p = turtle.Turtle()
p.speed(0)
p.pu()
p.setpos(100, 200)
p.pd()
p.hideturtle()

def fractal(i, n, cor):
    if n == 0:
        p.color(cor)
        p.begin_fill()
        p.forward(i)
        p.left(120)
        p.forward(i)
        p.left(120)
        p.forward(i)
        p.left(120)
        p.end_fill()
    else:
        fractal(i / 2, n - 1, 'darkred')
        p.forward(i / 2)
        fractal(i / 2, n - 1, 'red')
        p.left(120)
        p.forward(i / 2)
        p.right(120)
        fractal(i / 2, n - 1, 'pink')
        p.right(120)
        p.forward(i / 2)
        p.left(120)

fractal(200, 0, 'white')
fractal(200, 3, '')

janela.exitonclick()
