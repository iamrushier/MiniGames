# Created by Yashodhan Devdhar
import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=700)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle H
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=0.1, stretch_len=38)
paddle_a.penup()
paddle_a.goto(0, 310)

# Paddle -H
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=0.1, stretch_len=38)
paddle_a.penup()
paddle_a.goto(0, -311)

# Paddle -V
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=31, stretch_len=0.1)
paddle_a.penup()
paddle_a.goto(-380, 0)

# Paddle V
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=31, stretch_len=0.1)
paddle_a.penup()
paddle_a.goto(380, 0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 315)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y<260:
        y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y>-241:
        y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if y<260:
        y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y>-241:
        y -= 20
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Left and right
    if ball.xcor() > 370:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("bonus.wav", winsound.SND_ASYNC)

    elif ball.xcor() < -370:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("bonus.wav", winsound.SND_ASYNC)

    # Paddle and ball collisions
    if ball.xcor() < -330 and ball.xcor() > -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 330 and ball.xcor() < 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(330)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


