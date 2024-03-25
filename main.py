from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for key events to control the snake
screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")
game_is_on = True
while game_is_on:
    # Update the screen
    screen.update()
    # Pause briefly for smooth animation
    time.sleep(0.1)
    # Move the snake
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with the snake's body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Keep the window open until clicked
screen.exitonclick()
