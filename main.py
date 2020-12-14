from turtle import Screen
import time
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
# starting_position = ((0, 0), (-20, 0), (-40, 0))

snake = Snake()
food = Food()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_running = True
while game_running:
    screen.update()
    time.sleep(.3)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()



screen.exitonclick()
