from turtle import Turtle, Screen
import random
class Food(Turtle):
    def __init__(self):
        """Initialize the Food object."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        """Move the food to a random position."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)