import random
import turtle
import time
def goto(a,b):
    turtle.penup()
    turtle.goto(a,b)
    turtle.down()
def rectangle(a,b,c,d):
    goto(a,b)
    turtle.fillcolor("black")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(c)
        turtle.right(90)
        turtle.forward(d)
        turtle.right(90)
    turtle.end_fill()
you = system = 0
list1=["R","P","S"]
turtle.title("Game")
turtle.bgcolor("black")
turtle.pencolor("pink")
turtle.pensize(5)
turtle.ht()
turtle.speed("fast")
rectangle(-320,310,650,100)
goto(0,240)
turtle.write("Rock  Paper  scissors",align="center",font=("tahoma",30,"bold"))
rectangle(-320,200,325,50)
goto(-160,160)
turtle.write("YOU",align="center",font=("tahoma",20))
rectangle(5,200,325,50)
goto(160,160)
turtle.write("SYSTEM",align="center",font=("tahoma",20))
while True:
    rectangle(-320,140,325,50)
    goto(-160,100)
    turtle.write(you,align="center",font=("tahoma",20))
    rectangle(5,140,325,50)
    goto(160,100)
    turtle.write(system,align="center",font=("tahoma",20))
    rectangle(-320,80,325,400)
    rectangle(5,80,325,400)
    user=turtle.textinput("Game","please enter R=Rock  P=Paper  S=Scissors :")
    pc=random.choice(list1)
    goto(-160,-180)
    if user == "R":
        turtle.circle(80)
    elif user == "P":
        goto(-250,-50)
        for i in range(2):
            turtle.forward(200)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
    else:
        goto(-190,-80)
        turtle.circle(20)
        turtle.right(15)
        turtle.forward(150)
        goto(-198,-140)
        turtle.circle(20)
        goto(-198,-103)
        turtle.left(30)
        turtle.forward(160)
        turtle.right(15)
    goto(160,-180)
    if pc == "R":
        turtle.circle(80)
    elif pc == "P":
        goto(70,-50)
        for i in range(2):
            turtle.forward(200)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
    else:
        goto(210,-80)
        turtle.circle(20)
        turtle.right(160)
        turtle.forward(160)
        goto(210,-110)
        turtle.circle(20)
        turtle.right(40)
        turtle.forward(160)
        turtle.left(200)
    if (user == "R" and pc == "S" ) or (user == "P" and pc == "R") or (user == "S" and pc == "P"):
        you += 1
    elif user == pc:
        pass
    else:
        system += 1
    time.sleep(3)
turtle.done()