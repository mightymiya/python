import turtle
import random
screen=turtle.Screen()
screen.bgcolor("white")
dart=turtle.Turtle()
dart.color("black")
dart.shape("triangle")
dart.setheading(90)
dart.up()
dart.goto(0,-200)

balloon1=turtle.Turtle()
balloon1.color("green")
balloon1.shape("circle")

balloon2=turtle.Turtle()
balloon2.color("yellow")
balloon2.shape("circle")

balloon3=turtle.Turtle()
balloon3.color("blue")
balloon3.shape("circle")

balloon4=turtle.Turtle()
balloon4.color("pink")
balloon4.shape("circle")

balloon5=turtle.Turtle()
balloon5.color("red")
balloon5.shape("circle")

balloons=[balloon1,balloon2,balloon3,balloon4,balloon5]
for i in balloons:
    i.up()
    i.goto(random.randint(-300,300),random.randint(200,400))
def goleft():
    currentx=dart.xcor()
    dart.setx(currentx-20)
def goright():
    currentx=dart.xcor()
    dart.setx(currentx+20)
screen.listen()
screen.onkey(goleft,"a")
screen.onkey(goright,"d")
score=0
scoreboard=turtle.Turtle()
scoreboard.color("black")
scoreboard.up()
scoreboard.goto(-100,200)
scoreboard.write("score; "+str(score),font=("Arial" ,20))

while True:
    for i in balloons:
        i.sety(i.ycor()-3)
        if i.ycor()<-300:
            i.hideturtle()
            i.sety(300)
        
            i.showturtle()
    if dart.distance(balloon2)<15:
        score=score+2
        balloon2.hideturtle()
        balloon2.sety(300)
        balloon2.showturtle()
        scoreboard.clear()
        scoreboard.write("score; "+str(score),font=("Arial" ,20))
        
    if dart.distance(balloon4)<15:
        score=score+5
        balloon4.hideturtle()
        balloon4.sety(300)
        balloon4.showturtle()
        scoreboard.clear()
        scoreboard.write("score; "+str(score),font=("Arial" ,20))

    if dart.distance(balloon1)<15:
        score=score+1
        balloon1.hideturtle()
        balloon1.sety(300)
        balloon1.showturtle()
        scoreboard.clear()
        scoreboard.write("score; "+str(score),font=("Arial" ,20))

    if dart.distance(balloon3)<15:
        score=score-5
        balloon3.hideturtle()
        balloon3.sety(300)
        balloon3.showturtle()
        scoreboard.clear()
        scoreboard.write("score; "+str(score),font=("Arial" ,20))

    if dart.distance(balloon5)<15:
        turtle.write("game over")
        break

    if score==50:
        turtle.write("you win")
        break
    
 






''


























screen.mainloop()
