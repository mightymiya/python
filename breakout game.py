import turtle
screen=turtle.Screen()
screen.bgcolor("black")

dart=turtle.Turtle()
dart.color("white")
dart.shape("square")
dart.up()
dart.goto(0,-200)
ball=turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.up()

for i in range(5):
    for j in range(8):
        brickx=(-200+j*50)
        bricky=(200-i*50)
        brick=turtle.Turtle()
        brick.color("pink")
        brick.shape("square")
        brick.up()
        brick.goto(brickx,bricky)


def goleft():
    currentx=dart.xcor()
    dart.setx(currentx-20)

def goright():
    currentx=dart.xcor()
    dart.setx(currentx+20)
screen.listen()
screen.onkey(goleft,"a")
screen.onkey(goright,"d")
dx=2
dy=1
while True:
    ball.setx(ball.xcor()+dx)
    ball.sety(ball.ycor()+dy)
    
    











screen.mainloop()
