from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import (Scoreboard)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
# scoreboard.keep_score()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_running = True
while game_running:
    screen.update()
    time.sleep(.2)

    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.award_point()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 \
            or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_running = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_running = False
            scoreboard.game_over()

screen.exitonclick()
