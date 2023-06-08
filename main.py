from turtle import Turtle, Screen
from snakeobj import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
food = Food()
board = Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        board.score_update(0)
        food.food_generator()
        snake.add_segment()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        snake.reset()
        board.reset_score()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 15:
            snake.reset()
            board.reset_score()
board.check_highest_score()
board.score_update(1)
screen.exitonclick()
